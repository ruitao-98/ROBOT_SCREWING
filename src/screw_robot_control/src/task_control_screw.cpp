#include "screw_robot_control/jaka/task_control_screw.hpp"
#include <thread>
#include <chrono>

namespace screw_control {

ScrewControlServer::ScrewControlServer() : Node("screw_control") {
  RCLCPP_INFO(this->get_logger(), "Screw Control Server started.");

  // 初始化发布者
  current_pub_ = this->create_publisher<robot_msgs::msg::CurrentPub>("current_p", 10);
  width_pub_ = this->create_publisher<robot_msgs::msg::WidthPub>("width_p", 10);
    // 交互式控制循环（阻塞）
  // bool running = true;
  // char input;
  // while (running) {
  //   std::cout << "Enter 1 for screwing, 2 for width_recovery, 3 for width_reduce, 4 for screw_to_zero, or any other key to exit:" << std::endl;
  //   std::cin >> input;

  //   switch (input) {
  //     case '1':
  //       std::cout << "screwing" << std::endl;
  //       ef_.screwing_s1(200, 1.4, current_pub_, current_msg_);
  //       break;
  //     case '2':
  //       std::cout << "width_recovery" << std::endl;
  //       ef_.width_recovery();
  //       break;
  //     case '3':
  //       std::cout << "width_reduce_full_for_handover" << std::endl;
  //       ef_.width_reduce_full_for_handover(current_pub_, current_msg_, width_pub_, width_msg_);
  //       break;
  //     case '4':
  //       std::cout << "screw_to_zero" << std::endl;
  //       ef_.screw_to_zero();
  //       break;
  //     default:
  //       std::cout << "task stopped" << std::endl;
  //       running = false;
  //       break;
  //   }
  // }
  
  // 初始化 Action 服务端
  action_server_ = rclcpp_action::create_server<robot_msgs::action::Screw>(
      this,
      "screwactions",
      std::bind(&ScrewControlServer::handle_goal, this, std::placeholders::_1, std::placeholders::_2),
      std::bind(&ScrewControlServer::handle_cancel, this, std::placeholders::_1),
      std::bind(&ScrewControlServer::handle_accepted, this, std::placeholders::_1));
      RCLCPP_INFO(this->get_logger(), "Action server started.");
    }

// 当客户端发送一个新的 Action 目标（Screw::Goal）到服务端的 /screwactions 话题时，
// handle_goal 被调用，决定是否接受该目标。
rclcpp_action::GoalResponse ScrewControlServer::handle_goal(
    const rclcpp_action::GoalUUID &,
    std::shared_ptr<const robot_msgs::action::Screw::Goal> goal) {
  RCLCPP_INFO(this->get_logger(), "Received goal: %d", goal->num);
  return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
}

// 当客户端请求取消正在执行的 Action 目标时，handle_cancel 被调用，决定是否接受取消请求。
rclcpp_action::CancelResponse ScrewControlServer::handle_cancel(
    const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle) {
  RCLCPP_INFO(this->get_logger(), "Received cancel request for goal: %d", goal_handle->get_goal()->num);
  return rclcpp_action::CancelResponse::ACCEPT;
}
// 当 handle_goal 接受一个目标（返回 ACCEPT_AND_EXECUTE）后，handle_accepted 被调用，启动目标的实际执行。
void ScrewControlServer::handle_accepted(
    const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle) {
  // 在新线程中执行目标，避免阻塞
   execute(goal_handle);
}

void ScrewControlServer::execute(
    const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle) {
  const auto goal = goal_handle->get_goal();
  int num = goal->num;
  int result = 0;
  auto feedback = std::make_shared<robot_msgs::action::Screw::Feedback>();
  auto result_msg = std::make_shared<robot_msgs::action::Screw::Result>();

  RCLCPP_INFO(this->get_logger(), "Executing goal: %d", num);

  if (num == 0) {
    std::cout << "执行下一步旋拧装配" << std::endl;
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    result = ef_.screwing_s2(210, current_pub_, current_msg_);

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 1) {
    std::cout << "执行第一阶段的螺纹搜索" << std::endl;
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    std::this_thread::sleep_for(std::chrono::seconds(1));
    result = ef_.screwing_s1(200, 1, current_pub_, current_msg_);

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 2) {
    std::cout << "对准失败，卡住了，退出" << std::endl;
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    result = ef_.unscrew_to_zero(200);

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 3) {
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    result = ef_.width_recovery();
    std::this_thread::sleep_for(std::chrono::microseconds(100000)); // 0.1s

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 4) {
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    ef_.screw_to_zero();
    result = 4;

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 5) {
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    result = ef_.width_reduce_full_for_handover(current_pub_, current_msg_, width_pub_, width_msg_);

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  } else if (num == 6) {
    feedback->screw_status = 1.0;
    goal_handle->publish_feedback(feedback);

    ef_.width_increase(6, current_pub_, current_msg_, width_pub_, width_msg_);
    result = 2;

    feedback->screw_status = 0.0;
    goal_handle->publish_feedback(feedback);
  }

  // 设置结果
  if (!goal_handle->is_canceling()) {
    result_msg->result = result;
    goal_handle->succeed(result_msg);
    RCLCPP_INFO(this->get_logger(), "Final result: %d", result);
  } else {
    goal_handle->canceled(result_msg);
    RCLCPP_INFO(this->get_logger(), "Goal canceled");
  }
}

} // namespace screw_control

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<screw_control::ScrewControlServer>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}