#include "jaka/right_arm_control.hpp"
#include "jaka/screwing_tool.hpp"


namespace right_arm {
using namespace std;
using namespace Eigen;

RobotAdmittanceControl::RobotAdmittanceControl() : Node("screw_robot") {
    RCLCPP_INFO(this->get_logger(), "Robot Admittance Control Node has been started.");
    // 声明和初始化参数
    // pos_para_ = declare_parameter("pos_para", std::vector<double>{0.0, 0.0, 0.0});
    // ori_para_ = declare_parameter("ori_para", std::vector<double>{1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0});
    pos_para_ = {0.0, 0.0, 0.0};
    ori_para_ = {1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0};
   
    // 创建发布者
    force_pub_ = this->create_publisher<robot_msgs::msg::FtPub>("ft_data", 5);   
    status_pub_ = this->create_publisher<robot_msgs::msg::RobotStatus>("rob_status", 5);
    ref_pub_ = this->create_publisher<robot_msgs::msg::RefStatus>("ref_status", 5);
    cmd_pub_ = this->create_publisher<robot_msgs::msg::ControlCommand>("cmd_status", 5);     
    // 创建订阅者
    command_subs_ = this->create_subscription<robot_msgs::msg::ControlCommand>(
      "rob_command", 1, std::bind(&RobotAdmittanceControl::command_callback, this, std::placeholders::_1));
    // 创建服务
    srv_ = this->create_service<robot_msgs::srv::StartPose>(
    "get_param", std::bind(&RobotAdmittanceControl::ready_callback, this, std::placeholders::_1, std::placeholders::_2));
    // 初始化 Action 客户端
    client_ = rclcpp_action::create_client<robot_msgs::action::Screw>(this, "screwactions");
    if (!client_->wait_for_action_server(std::chrono::seconds(10))) {
        RCLCPP_ERROR(this->get_logger(), "Action server not available after 10 seconds");
        return;
      }
    
    selection_vector.resize(6);
    selection_vector<<1, 1, 1, 0, 0, 0;
    // 质量，刚度，阻尼
    adm_m.resize(6);
    adm_k.resize(6);
    adm_d.resize(6);
    wish_force.resize(6);
    wish_force << 0 ,0, 0, 0, 0, 0;

    adm_m << 3, 3, 4, 0.5, 0.5, 0.5;
    adm_k << 700.0, 700.0, 1300.0, 0.5, 0.5, 0.5;
    for (Eigen::Index i = 0; i < adm_m.size(); ++i) {
        adm_d[i] = 3 * sqrt(adm_m[i] * adm_k[i]);
    }
    adm_d[0] = 3.5 * sqrt(adm_m[0] * adm_k[0]);
    adm_d[1] = 3.5 * sqrt(adm_m[1] * adm_k[1]);
    adm_d[2] = 2.8 * sqrt(adm_m[2] * adm_k[2]);
    cout << "k" << adm_k[0] <<endl;
    cout << "d" << adm_d[0]<<endl;

    // 初始化机器人
    robot.login_in("192.168.3.201"); //right_arm
    robot.power_on();
    robot.enable_robot();
    // robot.set_tool_id(0);

    // reset();
    // go_to_pose();
    robot.servo_move_use_carte_NLF(50, 200, 800, 30, 60, 100);
    // robot.servo_speed_foresight(15, 0.03);
    robot.servo_move_enable(TRUE);
    robot.set_torque_sensor_mode(1);
    robot.set_compliant_type(1, 0);
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    robot.set_compliant_type(0,0);

    object_length << 0, 0, 0; 

    // eef_offset_basic << -0.0785, 0, 0.1169;
    // eef_offset_to_sensor_basic << -0.0785, 0, 0.0774;
    eef_offset_basic << -0.0772, 0, 0.1128;
    eef_offset_to_sensor_basic << -0.0772, 0, 0.0733;
    eef_offset = eef_offset_basic + object_length;
    // cout << "eef_offset" << eef_offset << endl;
    eef_offset_to_sensor = eef_offset_to_sensor_basic + object_length;

    tcp_set.tran.x = eef_offset[0]*1000; tcp_set.tran.y = eef_offset[1]*1000; tcp_set.tran.z = eef_offset[2]*1000;
    tcp_set.rpy.rx = 0; tcp_set.rpy.ry = -PI; tcp_set.rpy.rz = 0;
    robot.set_tool_data(6, &tcp_set, "screwtip");
    robot.set_tool_id(6);
    
    robot.get_tool_id(&id_ret);
    robot.get_tool_data(6,&tcp_ret);
    printf("id_using=%d \nx=%f, y=%f, z=%f\n", id_ret, tcp_ret.tran.x, tcp_ret.tran.y, tcp_ret.tran.z);
    printf("rx=%f, ry=%f, rz=%f\n", tcp_ret.rpy.rx, tcp_ret.rpy.ry, tcp_ret.rpy.rz);
    
    eef_offset_rotm_to_sensor = Eigen::AngleAxisd(-PI, Eigen::Vector3d::UnitZ()) *
                                Eigen::AngleAxisd(0, Eigen::Vector3d::UnitY()) *
                                Eigen::AngleAxisd(-PI, Eigen::Vector3d::UnitX());
    eef_offset_rotm = Eigen::AngleAxisd(-PI, Eigen::Vector3d::UnitZ()) *
                      Eigen::AngleAxisd(0, Eigen::Vector3d::UnitY()) *
                      Eigen::AngleAxisd(-PI, Eigen::Vector3d::UnitX());
}
//callback functions
void RobotAdmittanceControl::done_cb(
    const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::WrappedResult &result) {
    if (result.code == rclcpp_action::ResultCode::SUCCEEDED) {
        screw_execute_result_ = result.result->result;
        RCLCPP_INFO(this->get_logger(), "screw_execute_result: %d", result.result->result);
    } else {
        RCLCPP_ERROR(this->get_logger(), "Action failed with code: %d", static_cast<int>(result.code));
    }
}

void RobotAdmittanceControl::active_cb() {
    RCLCPP_INFO(this->get_logger(), "Action activated...");
}

void RobotAdmittanceControl::feedback_cb(
    const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::SharedPtr &,
    const std::shared_ptr<const robot_msgs::action::Screw::Feedback> feedback) {
    screw_execute_status_ = feedback->screw_status;
    RCLCPP_INFO(this->get_logger(), "Feedback: screw_status=%.2f", screw_execute_status_);
}

void RobotAdmittanceControl::command_callback(const robot_msgs::msg::ControlCommand::SharedPtr msg) {
    // 将消息中的 k 和 d 转换为 Eigen 向量
    adm_k = Eigen::Map<const Eigen::VectorXd>(msg->k.data(), msg->k.size());
    adm_d = Eigen::Map<const Eigen::VectorXd>(msg->d.data(), msg->d.size());
    RCLCPP_INFO(this->get_logger(), "Received control command: k_size=%ld, d_size=%ld", adm_k.size(), adm_d.size());
  }
  
void RobotAdmittanceControl::ready_callback(
      const std::shared_ptr<robot_msgs::srv::StartPose::Request>,
      std::shared_ptr<robot_msgs::srv::StartPose::Response> response) {
    RCLCPP_INFO(this->get_logger(), "Received request from MPC Node, sending response");
  
    // 设置响应
    response->success = true;
    response->message = "Robot Env is ready";
    response->pos_para = pos_para_;
    response->ori_para = ori_para_;
  
    // 打印参数（调试）
    RCLCPP_INFO(this->get_logger(), "pos_para=[%f, %f, %f], ori_para=[%f, %f, %f, %f, %f, %f, %f, %f, %f]",
                pos_para_[0], pos_para_[1], pos_para_[2],
                ori_para_[0], ori_para_[1], ori_para_[2], ori_para_[3], ori_para_[4], ori_para_[5], ori_para_[6], ori_para_[7], ori_para_[8]);
  }

void RobotAdmittanceControl::get_eef_pose(){
    link6_pos[0] = status.cartesiantran_position[0]/1000;
    link6_pos[1] = status.cartesiantran_position[1]/1000;
    link6_pos[2] = status.cartesiantran_position[2]/1000; //转化为米单位
    // 姿态欧拉角赋值
    current_rpy.rx = status.cartesiantran_position[3];
    current_rpy.ry = status.cartesiantran_position[4];
    current_rpy.rz = status.cartesiantran_position[5];
    // cout << current_rpy.rx << " " << current_rpy.ry << " "<< current_rpy.rz << endl;
    Rpy rpy;
    rpy.rx = current_rpy.rx; rpy.ry = current_rpy.ry; rpy.rz = current_rpy.rz;
    RotMatrix rot_matrix;
    // cout << "*******rpy_to_rot_matrix***********" << endl;

    robot.rpy_to_rot_matrix(&rpy, &rot_matrix);
    link6_rotm << rot_matrix.x.x, rot_matrix.x.y, rot_matrix.x.z,
                rot_matrix.y.x, rot_matrix.y.y, rot_matrix.y.z,
                rot_matrix.z.x, rot_matrix.z.y, rot_matrix.z.z;
    
    eef_rotm = link6_rotm * eef_offset_rotm;
    eef_pos = link6_pos + eef_rotm * (eef_offset_rotm.transpose() * eef_offset);
    eigen_rpy = eef_rotm.eulerAngles(2,1,0);
    // cout << "eef_offset=" << eef_offset[0] << eef_offset[1] << eef_offset[2] << endl;
    // cout << eef_pos << endl;
    // cout << eigen_rpy << endl;
}

void RobotAdmittanceControl::get_new_link6_pose(const Eigen::Vector3d& new_linear_eef, const Eigen::Matrix3d& new_angular_eef){
  // left_link6_pos = left_eef_pos - left_eef_rotm @ (self.left_eef_offset_rotm.T @ self.left_eef_offset)
  // left_link6_rotm = left_eef_rotm @ self.left_eef_offset_rotm.T
    // new_angular = new_angular_eef * eef_offset_rotm.transpose();
    // new_linear = new_linear_eef - (new_angular * eef_offset);
    new_linear = new_linear_eef - new_angular_eef * (eef_offset_rotm.transpose() * eef_offset);
    new_angular = new_angular_eef * eef_offset_rotm.transpose();
}

void RobotAdmittanceControl::updata_rotation(const Eigen::Matrix3d& current_rotm, const Eigen::Vector3d& angluar_disp, Eigen::Matrix3d& new_orientation){
    double angular_norm = angular_disp.norm();
    if (angular_norm < 1e-6) {
        new_orientation = current_rotm;
        RCLCPP_INFO(this->get_logger(), "Angular displacement too small, keeping current rotation.");
        return;
    }

    Eigen::AngleAxisd delta_rotation(angular_norm, angular_disp.normalized());
    Eigen::Matrix3d delta_rotm = delta_rotation.toRotationMatrix();
    if (!isRotationMatrix(delta_rotm)) {
        RCLCPP_WARN(this->get_logger(), "Delta rotation matrix is invalid!");
        new_orientation = current_rotm;
        return;
    }

    new_orientation = delta_rotm * current_rotm;
    if (!isRotationMatrix(new_orientation)) {
        RCLCPP_ERROR(this->get_logger(), "Generated rotation matrix is invalid!");
        new_orientation = current_rotm;
    }


    // Eigen::Matrix3d delta_rt;
    // delta_rt = Eigen::AngleAxisd(0, Eigen::Vector3d::UnitZ()) *
    //         Eigen::AngleAxisd(PI/2000, Eigen::Vector3d::UnitY()) *
    //         Eigen::AngleAxisd(0, Eigen::Vector3d::UnitX());
    // new_orientation = delta_rt * current_rotm;
}

bool RobotAdmittanceControl::isRotationMatrix(const Eigen::Matrix3d& matrix) {
    // 1. 检查是否为3x3矩阵（Eigen::Matrix3d已保证）
    
    // 2. 检查正交性：R^T * R 是否接近单位矩阵
    Eigen::Matrix3d identity = Eigen::Matrix3d::Identity();
    Eigen::Matrix3d product = matrix.transpose() * matrix;
    if (!product.isApprox(identity, 1e-6)) {
        return false;
    }

    // 3. 检查行列式是否接近1
    double det = matrix.determinant();
    if (std::abs(det - 1.0) > 1e-6) {
        return false;
    }

    return true;
}


void RobotAdmittanceControl::update_robot_state(){
    robot.get_robot_status(&status);
}

void RobotAdmittanceControl::get_tcp_force(){
    for (int i=0; i<6; i++){
        local_force[i] = status.torq_sensor_monitor_data.actTorque[i];
    }
    tcp_force.head<3>() = eef_offset_rotm_to_sensor.transpose() * local_force.head<3>();
    tcp_force.tail<3>() = eef_offset_to_sensor.cross(tcp_force.head<3>()) + eef_offset_rotm_to_sensor.transpose() * local_force.tail<3>();
    tcp_force.head<3>() = eef_rotm * tcp_force.head<3>();
    tcp_force.tail<3>() = eef_rotm * tcp_force.tail<3>();
    force_msg_.fx = tcp_force[0];
    force_msg_.fy = tcp_force[1];
    force_msg_.fz = tcp_force[2];
    force_msg_.tx = tcp_force[3];
    force_msg_.ty = tcp_force[4];
    force_msg_.tz = tcp_force[5];
    force_pub_->publish(force_msg_);
}

void RobotAdmittanceControl::tcp_admittance_control(){
    // 使用Eigen数组操作进行clip
    clipped_tcp_force = tcp_force.array().min(upper).max(lower);
    clipped_tcp_force = wish_force + clipped_tcp_force;
    e.head<3>() = eef_pos - eef_pos_d; //将基坐标系下的位置偏移转化为tcp坐标系下的偏移，后续所有计算都是在当前时刻的tcp坐标系下，计算下一时刻的数值
    Eigen::Matrix3d e_rotm = (eef_rotm * eef_rotm_d.transpose());
    Eigen::AngleAxisd angle_axis(e_rotm);
    // 获取旋转向量（旋转轴 * 旋转角度）
    Eigen::Vector3d rotation_vector = angle_axis.angle() * angle_axis.axis();
    e.tail<3>() = rotation_vector;
    e_dot = eef_vel;
    Eigen::VectorXd MA = clipped_tcp_force - adm_k.cwiseProduct(e) - adm_d.cwiseProduct(e_dot);
    Eigen::VectorXd adm_acc = MA.cwiseQuotient(adm_m);
    Eigen::VectorXd adm_vel = eef_vel + adm_acc * T;
    linear_disp = adm_vel.head(3) * T;
    angular_disp = adm_vel.tail(3) * T; 
    linear_disp = selection_vector.head<3>().cwiseProduct(linear_disp);
    angular_disp = selection_vector.tail<3>().cwiseProduct(angular_disp);
    // cout << "linear_disp" << linear_disp << endl;
    // cout << "angular_disp" << angular_disp << endl;
    // cout << "selection_vector" << selection_vector << endl;
    eef_vel = adm_vel;

}

void RobotAdmittanceControl::tcp_admittance_run(){
    robot.servo_move_enable(true);
    wish_force << 0, 0, 0, 0, 0, 0;  //期望力
    selection_vector<< 0, 0, 0, 0, 1, 0; //选择向量
                
    object_length << 0, 0, 0.021;   //m6*35螺丝 30 * 5.5
    eef_offset = eef_offset_basic + object_length;
    cout << "eef_offset" << eef_offset << endl;
    eef_offset_to_sensor = eef_offset_to_sensor_basic + object_length; //更新tcp

    tcp_set.tran.x = eef_offset[0]*1000; tcp_set.tran.y = eef_offset[1]*1000; tcp_set.tran.z = eef_offset[2]*1000;
    tcp_set.rpy.rx = 0; tcp_set.rpy.ry = -PI; tcp_set.rpy.rz = 0;
    robot.set_tool_data(6, &tcp_set, "screwtip");
    robot.set_tool_id(6);
    robot.get_tool_id(&id_ret);
    robot.get_tool_data(6,&tcp_ret);
    printf("id_using=%d \nx=%f, y=%f, z=%f\n", id_ret, tcp_ret.tran.x, tcp_ret.tran.y, tcp_ret.tran.z);
    printf("rx=%f, ry=%f, rz=%f\n", tcp_ret.rpy.rx, tcp_ret.rpy.ry, tcp_ret.rpy.rz);
    std::this_thread::sleep_for(std::chrono::milliseconds(3000)); 
    
    adm_m << 3, 3, 4, 0.5, 0.5, 0.5;
    adm_k << 700.0, 700.0, 1100.0, 0.5, 0.5, 0.5;
    for (Eigen::Index i = 0; i < adm_m.size(); ++i) {
        adm_d[i] = 2 * sqrt(adm_m[i] * adm_k[i]);
    }

    update_robot_state();
    get_tcp_force();
    get_eef_pose();
    eef_pos_d = eef_pos;
    eef_rotm_d = eef_rotm;
    int item = 0;
    while ((item < 40000) &&  (rclcpp::ok()))
    {   auto start_time = std::chrono::high_resolution_clock::now();
        update_robot_state();
        get_tcp_force();
        get_eef_pose();  //更新机器人状态

        eef_pos_d = eef_pos; 
        eef_rotm_d = eef_rotm;//期望的位置不断更新，始终保持是当前状态，期望的位姿保持不变

        item = item + 1;
        // 导纳控制的范畴
        tcp_admittance_control();
        
        linear_disp_clipped = linear_disp.cwiseMin(0.01).cwiseMax(-0.01);
        angluer_disp_clipped = angular_disp.cwiseMin(0.01).cwiseMax(-0.01); //此处获取了在tcp坐标系下机器人末端的位移偏量
        cout << "linear_disp_clipped "<< linear_disp_clipped[0] << " "<< linear_disp_clipped[1] << " "<< linear_disp_clipped[2] << endl;
        new_linear_eef = eef_pos + linear_disp_clipped; //最后将总偏移量再加到原始的tcp坐标上面去。
        // new_linear_eef = eef_pos;
        updata_rotation(eef_rotm, angluer_disp_clipped, new_rotm_eef);
        //fixed rotation
        //   new_rotm_eef = eef_rotm; 
        cout<<"new_eef_trans" << new_linear_eef[0] << " " << new_linear_eef[1] << " "<< new_linear_eef[2] << " "<< endl;
       
        get_new_link6_pose(new_linear_eef, new_rotm_eef);
        new_rotm.x.x = new_angular(0,0); new_rotm.y.x = new_angular(1,0); new_rotm.z.x = new_angular(2,0);
        new_rotm.x.y = new_angular(0,1); new_rotm.y.y = new_angular(1,1); new_rotm.z.y = new_angular(2,1);
        new_rotm.x.z = new_angular(0,2); new_rotm.y.z = new_angular(1,2); new_rotm.z.z = new_angular(2,2);
        robot.rot_matrix_to_rpy(&new_rotm, &new_rpy); //转欧拉角
        new_pos.rpy.rx = new_rpy.rx; new_pos.rpy.ry = new_rpy.ry; new_pos.rpy.rz = new_rpy.rz;

        new_pos.tran.x = new_linear[0] * 1000; new_pos.tran.y = new_linear[1] * 1000; new_pos.tran.z = new_linear[2] * 1000;
        // new_pos.rpy.rx = current_rpy.rx; new_pos.rpy.ry = current_rpy.ry; new_pos.rpy.rz = current_rpy.rz;
        cout<<"new_trans" << new_pos.tran.x << " " << new_pos.tran.y << " "<< new_pos.tran.z << " "<< endl;
        cout <<"new_rpy" << (new_pos.rpy.rx / PI) * 180 << "  " << (new_pos.rpy.ry / PI) * 180<< "  " << (new_pos.rpy.rz / PI) * 180<<"  " << endl; //new_rpy.rx不受导纳控制输出的影响，一开始就写死了
        cout << "_____________________________" << endl;
        robot.servo_p(&new_pos, ABS, loop_rate);
        std::this_thread::sleep_for(std::chrono::milliseconds(10)); 
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
        if (item % 200 == 0){
            cout << "item" << item << " excution time is"<< duration.count()<<"ms" << endl;}
    }

}

void RobotAdmittanceControl::print_eef(char choice){
    switch(choice) {
  
        case '1':
            object_length << 0, 0, 0.025;   //M12 六角头螺丝
            break;
        case '2':
            object_length << 0, 0, 0.016;   //3分螺母
            break; 
        case '3':
            object_length << 0, 0, 0.021;  //三通，3分
            break;
        case '4':
            object_length << 0, 0, 0.0355;   //m6*30螺丝 30 * 5.5
            break;
        case '5':
            object_length << 0, 0, 0.0925;   //m6*30螺丝 30 * 5.5
            break; 
        case '6':
            object_length << 0, 0, 0.082;   //m6*30螺丝 30 * 5.5
            break;  
    }
  
    eef_offset = eef_offset_basic + object_length;
    cout << "eef_offset" << eef_offset << endl;
    eef_offset_to_sensor = eef_offset_to_sensor_basic + object_length; //更新tcp
  
    update_robot_state();
    get_eef_pose();
  
    cout << "eef_pos"<< eef_pos << endl;
    cout << "eigen_rpy"<<eigen_rpy << endl;
  
  }

void RobotAdmittanceControl::linear_search(char choice_tcp){

    wish_force << 0, 0, -5, 0, 0, 0;  //期望力
    selection_vector<<1, 1, 1, 0, 0, 0; //选择向量
    adm_m << 3, 3, 3, 0.5, 0.5, 0.5;
    adm_k << 700.0, 700.0, 1200.0, 0.5, 0.5, 0.5;
    for (Eigen::Index i = 0; i < adm_m.size(); ++i) {
        adm_d[i] = 4 * sqrt(adm_m[i] * adm_k[i]);}
    adm_d[0] = 3.5 * sqrt(adm_m[0] * adm_k[0]);
    adm_d[1] = 3.5 * sqrt(adm_m[1] * adm_k[1]);
    adm_d[2] = 2.5 * sqrt(adm_m[2] * adm_k[2]);
    robot.set_compliant_type(1, 0);
    std::this_thread::sleep_for(std::chrono::milliseconds(200)); 
    robot.set_compliant_type(0,0);

    switch(choice_tcp) {

      case '1':
          object_length << 0, 0, 0.025;   //M12 六角头螺丝
          break; 

      case '2':
          object_length << 0, 0, 0.016;   //3分螺母
          break; 
      
      case '3':
          
          object_length << 0, 0, 0.021;  //三通，3分
          break;

      case '4':
          object_length << 0, 0, 0.0355;   //m6*30螺丝 30 * 5.5
          break; 
      case '5':
          object_length << 0, 0, 0.0925;   //handle
          break; 
      case '6':
          object_length << 0, 0, 0.082;   //Alan wrench
          break;  
      }

  eef_offset = eef_offset_basic + object_length;
  cout << "eef_offset" << eef_offset << endl;
  eef_offset_to_sensor = eef_offset_to_sensor_basic + object_length; //更新tcp

  robot.servo_move_enable(true);
  //直线搜索***********************************************************************************
  update_robot_state();
  get_tcp_force();
  get_eef_pose();
  eef_pos_d = eef_pos;
  eef_rotm_d = eef_rotm;

  int item = 0;

  while ((item < 7000) && (rclcpp::ok()))
  {   
      auto start_time = std::chrono::high_resolution_clock::now();
      // 导纳控制的范畴
      update_robot_state();
      get_tcp_force();
      get_eef_pose();  //更新机器人状态

      item = item + 1;

      eef_pos_d = eef_pos; //期望的位置不断更新，始终保持是当前状态，期望的位姿保持不变
      eef_rotm_d = eef_rotm;

      if (tcp_force[2] > 3){
          cout << "-----------linear search stopped------------" << endl;
          break;
      }

      // for ros pub
    //   pose_p.X = eef_pos[0];
    //   pose_p.Y = eef_pos[1];
    //   pose_p.Z = eef_pos[2];
    //   pose_p.RX = eigen_rpy[2];
    //   pose_p.RY = eigen_rpy[1];
    //   pose_p.RZ = eigen_rpy[0];
    //   pose_p.FX = tcp_force[0];
    //   pose_p.FY = tcp_force[1];
    //   pose_p.FZ = tcp_force[2];
    //   pose_p.theta = 0;
    //   pos_pub_6.publish(pose_p);
      /////////////////////

      tcp_admittance_control();
      linear_disp_clipped = linear_disp.cwiseMin(0.01).cwiseMax(-0.01);
      angluer_disp_clipped = angular_disp.cwiseMin(0.01).cwiseMax(-0.01); //此处获取了在tcp坐标系下机器人末端的位移偏量

      new_linear_eef = eef_pos + eef_rotm * linear_disp_clipped; //最后将总偏移量再加到原始的tcp坐标上面去。
      //fixed rotation
      // new_rotm_eef = eef_rotm; 

      updata_rotation(eef_rotm, angluer_disp_clipped, new_rotm_eef);

      get_new_link6_pose(new_linear_eef, new_rotm_eef);
      new_rotm.x.x = new_angular(0,0); new_rotm.y.x = new_angular(1,0); new_rotm.z.x = new_angular(2,0);
      new_rotm.x.y = new_angular(0,1); new_rotm.y.y = new_angular(1,1); new_rotm.z.y = new_angular(2,1);
      new_rotm.x.z = new_angular(0,2); new_rotm.y.z = new_angular(1,2); new_rotm.z.z = new_angular(2,2);
      robot.rot_matrix_to_rpy(&new_rotm, &new_rpy); //link6 转欧拉角

      new_pos.tran.x = new_linear[0] * 1000; new_pos.tran.y = new_linear[1] * 1000; new_pos.tran.z = new_linear[2] * 1000;
      new_pos.rpy.rx = new_rpy.rx; new_pos.rpy.ry = new_rpy.ry; new_pos.rpy.rz = new_rpy.rz;

      robot.servo_p(&new_pos, ABS, loop_rate);
      // std::this_thread::sleep_for(std::chrono::milliseconds(8)); 
      auto end_time = std::chrono::high_resolution_clock::now();
      auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
      if (item % 260 == 0){
          cout << "linear search item" << item << " excution time is"<< duration.count()<<"ms" << endl;
      }
  }
}

void RobotAdmittanceControl::passive_fine(){
  update_robot_state();
  get_tcp_force();
  get_eef_pose();
  wish_force << 0, 0, -10, 0, 0, 0;  //期望力
  selection_vector<<1, 1, 1, 0, 0, 0; //选择向量
  adm_m << 3, 3, 3, 0.5, 0.5, 0.5;
  adm_k << 700.0, 700.0, 1300.0, 0.5, 0.5, 0.5;
  for (Eigen::Index i = 0; i < adm_m.size(); ++i) {
      adm_d[i] = 4 * sqrt(adm_m[i] * adm_k[i]);
  }
  adm_d[0] = 3.5 * sqrt(adm_m[0] * adm_k[0]);
  adm_d[1] = 3.5 * sqrt(adm_m[1] * adm_k[1]);
  adm_d[2] = 7.5 * sqrt(adm_m[2] * adm_k[2]);
  eef_pos_d = eef_pos;
  eef_rotm_d = eef_rotm;
  Eigen::Vector3d init_height = {0.0, 0.0, 0.0};
  Eigen::Vector3d end_height = {0.0, 0.0, 0.0};
  int flag = 1; //初始化，一开始是搜索状态
  screw_execute_status_ = 2; //初始化，肯定是未运行的；
  new_rpy.rx = current_rpy.rx; 
  new_rpy.ry = current_rpy.ry;
  screw_execute_result_ = 9; //不需要对其进行初始化，一开始他没有结果
  int max_rotations = 2;
  int rotation_item = 0;
  // int theta_index = 1;
  double distance_threhold = 0.7;  // 单位 mm 
  auto goal_msg = robot_msgs::action::Screw::Goal();
  while (rclcpp::ok()){
      Eigen::Vector3d delta_height = eef_rotm.transpose() * (init_height - end_height);
      // 判断是否要执行下一个期望位姿
      if (screw_execute_result_ == 2){ 
          cout << "装配完成，退出" << endl;
          // 装配完成
          flag = 3;
          break;}

      else if ((screw_execute_result_ == 0) && (abs(delta_height[2])>(distance_threhold /1000))){
          cout << "delta_height[2] = " << delta_height[2] << endl;
          cout << "flag = 0, 对准成功，进入下一步装配" << endl;
          flag = 0;
          if (rotation_item >= max_rotations){
              cout << "装配成功，但是提前结束，不必拧紧" << endl;
              break;
          }
          rotation_item = rotation_item + 1;
          // 对准成功，进入下一步装配，完全旋拧
      }
      else if ((screw_execute_result_ == 0) && (abs(delta_height[2])<(distance_threhold /1000))){
          cout << "delta_height[2] = " << delta_height[2] << endl;
          cout << "仍然没有对准" << endl;
          flag = 1;
      }

      else if (screw_execute_result_ == 1){
          cout << "flag = 2, 卡住了，回退，进入下一个搜索" << endl;
          flag = 2;
          // 卡住了，回退，进入下一个搜索
      }

      int item = 0;
      screw_execute_status_ = 2; //每一次搜索，都把状态置为2，表示还没开始运行
      // int temp_flag = 1; //记录一开始高度的标志位
      cout << "开始运行" << endl;
      update_robot_state();
      get_eef_pose();
      eef_pos_d = eef_pos;
      while ((item < 5000)&&  (rclcpp::ok()))
      {  
          if ((screw_execute_status_ == 2) && (item >= 10))  //直接旋拧一般物体：320 
          {   // item_flag = 1; //表示已经开始执行了
            cout << "\r" <<" start to send message " << flush;
            update_robot_state();
            get_eef_pose(); 
 
            goal_msg.num = flag; // 0 直接运行后续装配过程 1 运行第一阶段，接着搜索 2 出现错误，回退
            auto send_goal_options = rclcpp_action::Client<robot_msgs::action::Screw>::SendGoalOptions();
            send_goal_options.goal_response_callback =
                std::bind(&RobotAdmittanceControl::active_cb, this);
            send_goal_options.feedback_callback =
                [this](rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::SharedPtr handle,
                       const std::shared_ptr<const robot_msgs::action::Screw::Feedback> feedback) {
                  this->feedback_cb(handle, feedback);
                };
            send_goal_options.result_callback =
                [this](const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::WrappedResult &result) {
                  this->done_cb(result);
                };
            
            // send_goal_options.feedback_callback =
            //     std::bind(&RobotAdmittanceControl::feedback_cb, this, std::placeholders::_1, std::placeholders::_2);
            // send_goal_options.result_callback =
            //     std::bind(&RobotAdmittanceControl::done_cb, this, std::placeholders::_1, std::placeholders::_2);

            client_->async_send_goal(goal_msg, send_goal_options);
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
          }

          if (screw_execute_status_ == 0){ //screw_execute_status = 0 表示运行结束了
              // 执行器运行结束了，可以切换了
              cout << " screw tool excution finish! break! " << endl;
              end_height = eef_pos; //记录结束的位置
              break;
          }

          if ((screw_execute_status_ == 1) && (item == 330)){
              init_height = eef_pos; //记录一下一开始的位置
              cout << " temp_flag = 0" << endl;
          }
              
          auto start_time = std::chrono::high_resolution_clock::now();
          eef_pos_d[2] = eef_pos[2];
          eef_rotm_d = eef_rotm;

          item = item + 1;

          // 导纳控制的范畴
          update_robot_state();
          get_tcp_force();
          get_eef_pose();

        //   pose_p.X = eef_pos[0];
        //   pose_p.Y = eef_pos[1];
        //   pose_p.Z = eef_pos[2];
        //   pose_p.RX = eigen_rpy[0];
        //   pose_p.RY = eigen_rpy[1];
        //   pose_p.RZ = eigen_rpy[2];
        //   pose_p.FX = tcp_force[0];
        //   pose_p.FY = tcp_force[1];
        //   pose_p.FZ = tcp_force[2];
        //   pose_p.theta = 0;
        //   pos_pub_6.publish(pose_p);

          tcp_admittance_control();
          
          linear_disp_clipped = linear_disp.cwiseMin(0.01).cwiseMax(-0.01);
          angluer_disp_clipped = angular_disp.cwiseMin(0.01).cwiseMax(-0.01); //此处获取了在tcp坐标系下机器人末端的位移偏量
          //我们需要在此处对其进行修改，上述偏量经过选择向量的修改只剩z方向的偏移了，我们再加上x,y方向的偏移。
          linear_disp_clipped = linear_disp_clipped;
          new_linear_eef = eef_pos + eef_rotm * linear_disp_clipped; //最后将总偏移量再加到原始的tcp坐标上面去。

          updata_rotation(eef_rotm, angluer_disp_clipped, new_rotm_eef);
          get_new_link6_pose(new_linear_eef, new_rotm_eef);
          new_pos.tran.x = new_linear[0] * 1000; new_pos.tran.y = new_linear[1] * 1000; new_pos.tran.z = new_linear[2] * 1000;

          new_rotm.x.x = new_angular(0,0); new_rotm.y.x = new_angular(1,0); new_rotm.z.x = new_angular(2,0);
          new_rotm.x.y = new_angular(0,1); new_rotm.y.y = new_angular(1,1); new_rotm.z.y = new_angular(2,1);
          new_rotm.x.z = new_angular(0,2); new_rotm.y.z = new_angular(1,2); new_rotm.z.z = new_angular(2,2);
          robot.rot_matrix_to_rpy(&new_rotm, &new_rpy); //转欧拉角
          new_pos.rpy.rx = new_rpy.rx; new_pos.rpy.ry = new_rpy.ry; new_pos.rpy.rz = new_rpy.rz;

          robot.servo_p(&new_pos, ABS, loop_rate);

          auto end_time = std::chrono::high_resolution_clock::now();
          auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
          if ( item % 500 == 0 ){
              cout << "insertion item" << item << " excution time is"<< duration.count()<<"ms" << endl;
          }
          rclcpp::spin_some(this->shared_from_this());
      }
  }
}

void RobotAdmittanceControl::grasp_obj(){
    auto goal_msg = robot_msgs::action::Screw::Goal();
    goal_msg.num = 5;
    auto send_goal_options = rclcpp_action::Client<robot_msgs::action::Screw>::SendGoalOptions();
    send_goal_options.goal_response_callback =
        std::bind(&RobotAdmittanceControl::active_cb, this);
    send_goal_options.feedback_callback =
        [this](rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::SharedPtr handle,
               const std::shared_ptr<const robot_msgs::action::Screw::Feedback> feedback) {
          this->feedback_cb(handle, feedback);
        };
    send_goal_options.result_callback =
        [this](const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::WrappedResult &result) {
          this->done_cb(result);
        };
    
    client_->async_send_goal(goal_msg, send_goal_options);
    std::this_thread::sleep_for(std::chrono::milliseconds(50));
    rclcpp::Rate rate(100); // 100 Hz，控制循环频率
    while (rclcpp::ok() && screw_execute_status_ != 0) {
    rclcpp::spin_some(this->shared_from_this());// 处理回调
    rate.sleep(); // 控制循环频率
    }
}

void RobotAdmittanceControl::robot_finish(){
    // 机器人回退
    robot.servo_move_enable(false);
    update_robot_state();
    get_eef_pose();
    linear_disp<< 0, 0, 0.04;
    new_linear_eef = eef_pos + eef_rotm * linear_disp;
    new_rotm_eef = eef_rotm;
    get_new_link6_pose(new_linear_eef, new_rotm_eef);
    new_pos.tran.x = new_linear[0] * 1000; new_pos.tran.y = new_linear[1] * 1000; new_pos.tran.z = new_linear[2] * 1000;
    new_pos.rpy.rx = new_rpy.rx; new_pos.rpy.ry = new_rpy.ry; new_pos.rpy.rz = new_rpy.rz;
    robot.linear_move(&new_pos, ABS, true, 10);

    std::this_thread::sleep_for(std::chrono::milliseconds(200));
    auto goal_msg = robot_msgs::action::Screw::Goal();
    goal_msg.num = 4;
    auto send_goal_options = rclcpp_action::Client<robot_msgs::action::Screw>::SendGoalOptions();
    send_goal_options.goal_response_callback =
        std::bind(&RobotAdmittanceControl::active_cb, this);
    send_goal_options.feedback_callback =
        [this](rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::SharedPtr handle,
               const std::shared_ptr<const robot_msgs::action::Screw::Feedback> feedback) {
          this->feedback_cb(handle, feedback);
        };
    send_goal_options.result_callback =
        [this](const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::WrappedResult &result) {
          this->done_cb(result);
        };
    client_->async_send_goal(goal_msg, send_goal_options);
    rclcpp::Rate rate(100); // 100 Hz，控制循环频率
    while (rclcpp::ok() && screw_execute_result_ != 4) {
    rclcpp::spin_some(this->shared_from_this()); // 处理回调
    rate.sleep(); // 控制循环频率
    }
}

void RobotAdmittanceControl::go_to_pose(char choice_tcp){
    CartesianPose goal_pose;
    char input;

    switch(choice_tcp) {

        case '1':
            object_length << 0, 0, 0.025;   //M12 六角头螺丝
            break; 
        case '2':
            object_length << 0, 0, 0.016;   //3分螺母
            break; 
        case '3':
            object_length << 0, 0, 0.021;  //三通，3分
            break;
        case '4':
            object_length << 0, 0, 0.0355;   //m6*35螺丝 30 * 5.5
            break;  
    }

    eef_offset = eef_offset_basic + object_length;
    eef_offset_to_sensor = eef_offset_to_sensor_basic + object_length; //更新tcp

    std::cout << "Enter 1-3 to select the goal position:" << std::endl;
    std::cin >> input;
    

    double angle;
    angle = 4.5 * PI / 180;
    switch(input) {  //双臂实验标定结果

      case '1':
          // angle = 2 * PI / 180;
          goal_pose.tran.x = -0.286045; goal_pose.tran.y = 0.337516 + 0.005+0.025; goal_pose.tran.z = -0.0174+0.002;
          goal_pose.rpy.rx = 0 + angle; goal_pose.rpy.ry = 0; goal_pose.rpy.rz =  3.14159;  // m6 螺丝

          // goal_pose.tran.x = -0.20941; goal_pose.tran.y = 0.370286 + 0.005; goal_pose.tran.z = 0.0429057;
          // goal_pose.rpy.rx = 0 + angle; goal_pose.rpy.ry = 0; goal_pose.rpy.rz =  3.14159;  // 三通
          break;

      case '2':
          // angle = 1 * PI / 180;
          goal_pose.tran.x = -0.272948; goal_pose.tran.y =  0.337422 + 0.0036; goal_pose.tran.z = 0.0387647 + 0.0012;
          goal_pose.rpy.rx = 0 + angle; goal_pose.rpy.ry = 0; goal_pose.rpy.rz = 3.14159; //m12-flat

          // goal_pose.tran.x = -0.285672+0.00; goal_pose.tran.y =  0.387309 + 0.0; goal_pose.tran.z = 0.0342756 + 0.002;
          // goal_pose.rpy.rx = 0 + angle; goal_pose.rpy.ry = 0; goal_pose.rpy.rz = 3.14159; //m12-nonflat
 
          break; // 添加break语句
      
      case '3':
          // angle = 2 * PI / 180;
          goal_pose.tran.x = -0.285849; goal_pose.tran.y =  0.337506 + 0.0036; goal_pose.tran.z = 0.0488019 + 0.0012;
          goal_pose.rpy.rx = 0 + angle ; goal_pose.rpy.ry = 0; goal_pose.rpy.rz =  3.14159; //螺母
          break; // 添加break语句

      default:
          // 程序结束
          std::cout << "task stoped" << std::endl;
      }

      eef_pos << goal_pose.tran.x, goal_pose.tran.y, goal_pose.tran.z;
      Rpy rpy;
      rpy.rx = goal_pose.rpy.rx; rpy.ry = goal_pose.rpy.ry; rpy.rz = goal_pose.rpy.rz;
      RotMatrix rot_matrix;
      robot.rpy_to_rot_matrix(&rpy, &rot_matrix);
      eef_rotm << rot_matrix.x.x, rot_matrix.x.y, rot_matrix.x.z,
                  rot_matrix.y.x, rot_matrix.y.y, rot_matrix.y.z,
                  rot_matrix.z.x, rot_matrix.z.y, rot_matrix.z.z;
      get_new_link6_pose(eef_pos, eef_rotm);

      new_rotm.x.x = new_angular(0,0); new_rotm.y.x = new_angular(1,0); new_rotm.z.x = new_angular(2,0);
      new_rotm.x.y = new_angular(0,1); new_rotm.y.y = new_angular(1,1); new_rotm.z.y = new_angular(2,1);
      new_rotm.x.z = new_angular(0,2); new_rotm.y.z = new_angular(1,2); new_rotm.z.z = new_angular(2,2);
      robot.rot_matrix_to_rpy(&new_rotm, &new_rpy); //转欧拉角

      new_pos.tran.x = new_linear[0] * 1000; new_pos.tran.y = new_linear[1] * 1000; new_pos.tran.z = new_linear[2] * 1000;
      new_pos.rpy.rx = new_rpy.rx; new_pos.rpy.ry = new_rpy.ry; new_pos.rpy.rz = new_rpy.rz;
      cout << new_pos.tran.x <<" "<< new_pos.tran.y <<" "<< new_pos.tran.z << endl;
      cout << new_pos.rpy.rx * 180 / PI <<" "<< new_pos.rpy.ry * 180 / PI <<" "<< new_pos.rpy.rz * 180 / PI << endl;
      robot.servo_move_enable(false);
      robot.linear_move(&new_pos, ABS, TRUE, 25);
}

void RobotAdmittanceControl::reset(){
    // -np.pi / 3, np.pi / 2, np.pi * 3 / 4, np.pi * 1 / 4, -np.pi / 2, np.pi / 2
    cout<< "reset the robot"<<endl;
    JointValue right_joint_pos = { -PI/3, PI/3, 2*PI/3, PI/2, -PI/2, PI/2 };  //标准实验，双臂协作时的零点
    robot.joint_move(&right_joint_pos, ABS, true, 0.15);

    // JointValue left_joint_pos = { -60.283 * PI / 180, 74.928 * PI / 180, 132.499 * PI / 180, 62.573 * PI / 180, -90 * PI / 180, 39.717 * PI / 180 }; //只做单臂实验的领零点
    // robot.joint_move(&left_joint_pos, ABS, true, 0.1);
    cout<< "the robot was resetted"<<endl;
    }
}

int main(int argc, char **argv) {
    std::cout << "test " << std::endl;
    rclcpp::init(argc, argv);
    std::cout << "test " << std::endl;
    auto node = std::make_shared<right_arm::RobotAdmittanceControl>();

    bool running = true;
    char input;
    char choice_tcp;
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time, end_time;
    std::chrono::milliseconds duration;

    while (running && rclcpp::ok()){
        std::cout << "1--> test program || 2--> go to reset pose " << std::endl;
        std::cout << "3--> go to goal pose || 4--> screw action " << std::endl;
        std::cout << "5--> grasp obj || 6--> get tcp for calibration " << std::endl;
        std::cin >> input;
        switch(input) {
            case '1':

                std::cout << "test program" << std::endl;
                // robot_control.go_to_pose();
                node->tcp_admittance_run();
                break;

            case '2':

                std::cout << "go to reset pose" << std::endl;
                // robot_control.tcp_admittance_run();
                node->reset();
                break;

            case '3':
                std::cout << "Enter 1-3 to select the tcp:" << std::endl;
                std::cout << "1--> M12 六角头 || 2--> 3分螺母 || 3--> 3分三通 || 4--> m6x30" << std::endl;
                std::cin >> choice_tcp;

                std::cout << "go to goal pose" << std::endl;
                node->go_to_pose(choice_tcp);
                break;
            
            case '4':

                std::cout << "screw action" << std::endl;
                // robot_control.screw_assembly_search();
                std::cout << "Enter 1-3 to select the tcp:" << std::endl;
                std::cout << "1--> M12 六角头 || 2--> 3分螺母 || 3--> 3分三通 || 4--> m6x30" << std::endl;
                std::cin >> choice_tcp;

                start_time = std::chrono::high_resolution_clock::now(); //不能在case里面初始化变量
                node->linear_search(choice_tcp);
                end_time = std::chrono::high_resolution_clock::now();
                duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
                std::cout << " linear search time is "<< duration.count()<<" ms" << std::endl;
                start_time = std::chrono::high_resolution_clock::now();
                // node->pos_search();
                // node->pos_ori_search();
                end_time = std::chrono::high_resolution_clock::now();
                duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
                std::cout << " pos search time is "<< duration.count()<<" ms" << std::endl;

                start_time = std::chrono::high_resolution_clock::now();
                // std::this_thread::sleep_for(std::chrono::seconds(2));
                // node->ori_fine();
                node->passive_fine();
                end_time = std::chrono::high_resolution_clock::now();
                duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time-start_time);
                std::cout << " ori search time is "<< duration.count()<<" ms" << std::endl;
                node->robot_finish();
                break;

            case '5':
                node->grasp_obj();
                break;

            case '6':
                std::cout << "Enter 1-3 to select the tcp:" << std::endl;
                std::cout << "1--> M12 六角头 || 2--> 3分螺母 || 3--> 3分三通 || 4--> m6x30" << std::endl;
                std::cin >> choice_tcp;
                node->print_eef(choice_tcp);
                break;

            default:
                std::cout << "Exiting program. Goodbye!" << std::endl;
                running = false;
                break;
        }
    }

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
