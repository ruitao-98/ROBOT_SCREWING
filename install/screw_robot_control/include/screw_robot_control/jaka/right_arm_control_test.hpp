#include <vector>
#include "jaka/JAKAZuRobot.h"
#include <stdio.h>
#include <thread>
#include "Eigen/Dense"
#include "Eigen/Core"
#include "Eigen/Geometry"
#include "Eigen/StdVector"
#include <mutex>
#include "jaka/jktypes.h"
#include <rclcpp/rclcpp.hpp>
// 消息类型
// #include <robot_msgs/msg/ft_pub.h>
#include <robot_msgs/msg/ft_pub.hpp>
#include <rclcpp_action/rclcpp_action.hpp>
#include <robot_msgs/action/screw.hpp>
#include <robot_msgs/msg/robot_status.hpp>
#include <robot_msgs/msg/ref_status.hpp>
#include <robot_msgs/msg/control_command.hpp>
#include <robot_msgs/srv/start_pose.hpp>

namespace jaka {
    using Quaternion = ::Quaternion; // 创建别名
}

namespace right_arm_test{
class RobotAdmittanceControl : public rclcpp::Node {
    public:
    RobotAdmittanceControl();

    void reset();
    void update_robot_state();
    void go_to_pose(char choice_tcp);
    void tcp_admittance_control();
    void get_eef_pose();
    
    void updata_rotation(const Eigen::Matrix3d& current_rotm, const Eigen::Vector3d& angluar_disp, Eigen::Matrix3d& new_orientation);
    void get_new_link6_pose(const Eigen::Vector3d& new_linear_eef, const Eigen::Matrix3d& new_angular_eef);
    // void ros_init(int argc, char** argv);
    
    void get_robot_pose();
    void get_world_force();
    void get_tcp_force();
    void start();
    void linear_search(char choice_tcp);
    void ori_fine();
    void robot_finish();
    void grasp_obj();
    void passive_fine();
    void print_eef(char choice);
    void tcp_admittance_run();

    bool isRotationMatrix(const Eigen::Matrix3d& matrix);

private:
    // 参数
    Eigen::VectorXd adm_m;
    Eigen::VectorXd adm_k;
    Eigen::VectorXd adm_d;

    Eigen::VectorXd world_force = Eigen::VectorXd::Zero(6);
    Eigen::VectorXd local_force = Eigen::VectorXd::Zero(6);
    Eigen::VectorXd tcp_force = Eigen::VectorXd::Zero(6);

    Eigen::Matrix3d link6_rotm;
    Eigen::Vector3d link6_pos;

    Eigen::Matrix3d eef_rotm;
    Eigen::Vector3d eef_pos;
    Eigen::Vector3d eigen_rpy;


    // std::thread excution_thread;
    // std::thread sensor_thread;
    
    //jaka 库相关声明
    Rpy current_rpy;
    RotMatrix current_rotm;

    int id_ret;
    JAKAZuRobot robot;
    RobotStatus status;
    CartesianPose cart;
    CartesianPose new_pos;
    RotMatrix new_rotm;
    Rpy new_rpy;
    CartesianPose tcp_set;
    CartesianPose tcp_ret;

    // ROS相关成员变量
    // 发布者
    rclcpp::Publisher<robot_msgs::msg::FtPub>::SharedPtr force_pub_;
    rclcpp::Publisher<robot_msgs::msg::RobotStatus>::SharedPtr status_pub_;
    rclcpp::Publisher<robot_msgs::msg::RefStatus>::SharedPtr ref_pub_;
    rclcpp::Publisher<robot_msgs::msg::ControlCommand>::SharedPtr cmd_pub_;
    // 订阅者
    rclcpp::Subscription<robot_msgs::msg::ControlCommand>::SharedPtr command_subs_;
    // 服务
    rclcpp::Service<robot_msgs::srv::StartPose>::SharedPtr srv_;
    // 消息实例（可选，取决于发布频率）
    robot_msgs::msg::FtPub force_msg_;
    robot_msgs::msg::RobotStatus status_msg_;
    robot_msgs::msg::RefStatus ref_msg_;
    // 参数
    // std::vector<double> pos_para_;
    // std::vector<double> ori_para_;

    std::array<double, 3> pos_para_;
    std::array<double, 9> ori_para_;

    // Action 客户端
    rclcpp_action::Client<robot_msgs::action::Screw>::SharedPtr client_;
    
    void active_cb();
    void feedback_cb(
        const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::SharedPtr &handle,
        const std::shared_ptr<const robot_msgs::action::Screw::Feedback> feedback); // 更新为 const
    void done_cb(
        const rclcpp_action::ClientGoalHandle<robot_msgs::action::Screw>::WrappedResult &result);
    // 回调函数
    void command_callback(const robot_msgs::msg::ControlCommand::SharedPtr msg);
    void ready_callback(
        const std::shared_ptr<robot_msgs::srv::StartPose::Request> request,
        std::shared_ptr<robot_msgs::srv::StartPose::Response> response);

                
    const double PI = 3.1415926;

    // std::mutex robot_mutex;
    int loop_rate = 1; //loop_rate * 8ms = real_rate
    double T = loop_rate * 0.008;

    Eigen::Vector3d eef_offset;
    Eigen::Vector3d eef_offset_basic;
    Eigen::Vector3d object_length;
    Eigen::Matrix3d eef_offset_rotm;
    Eigen::Vector3d eef_offset_to_sensor;
    Eigen::Vector3d eef_offset_to_sensor_basic;
    Eigen::Matrix3d eef_offset_rotm_to_sensor;
    jaka::Quaternion current_eef_quat;
    RotMatrix current_eef_rotm;

     // 定义力上下限
    double lower = -30.0;
    double upper = 30.0;


    //导纳控制相关变量
    Eigen::VectorXd selection_vector;
    Eigen::VectorXd clipped_world_force;
    Eigen::VectorXd clipped_tcp_force;
    Eigen::VectorXd wish_force;


    Eigen::Vector3d new_linear;
    Eigen::Matrix3d new_angular;

    Eigen::Vector3d eef_pos_d;
    Eigen::Matrix3d eef_rotm_d;
    Eigen::Matrix3d eef_rotm_d_modified;
    Eigen::VectorXd eef_vel = Eigen::VectorXd::Zero(6);
    Eigen::VectorXd e = Eigen::VectorXd::Zero(6);
    Eigen::VectorXd e_dot = Eigen::VectorXd::Zero(6);
    Eigen::Vector3d linear_disp;
    Eigen::Vector3d angular_disp;

    Eigen::Vector3d linear_disp_clipped;
    Eigen::Vector3d angluer_disp_clipped;
    Eigen::Vector3d new_linear_eef;
    Eigen::Matrix3d new_rotm_eef;

    int screw_execute_result_; //末端执行器运行结果 
    // 0：未卡
    // 1：卡住了
    // 2：全部运行结束
    
    int screw_execute_status_; //末端执行器运行结果 
    // 0：运行后
    // 1：正在运行
    // 2: 运行前

};

}