#include <rclcpp/rclcpp.hpp>
#include <rclcpp_action/rclcpp_action.hpp>
#include <robot_msgs/action/screw.hpp>
#include <robot_msgs/msg/current_pub.hpp>
#include <robot_msgs/msg/width_pub.hpp>
#include <screw_robot_control/jaka/screwing_tool.hpp> // 假设 endeffector 定义在此

namespace screw_control {

class ScrewControlServer : public rclcpp::Node {
public:
  ScrewControlServer();

private:
  // Action 服务端
  rclcpp_action::Server<robot_msgs::action::Screw>::SharedPtr action_server_;
  // 发布者
  rclcpp::Publisher<robot_msgs::msg::CurrentPub>::SharedPtr current_pub_;
  rclcpp::Publisher<robot_msgs::msg::WidthPub>::SharedPtr width_pub_;
  // 消息实例
  robot_msgs::msg::CurrentPub current_msg_;
  robot_msgs::msg::WidthPub width_msg_;
  // 末端执行器
  endeffector ef_;

  // Action 回调
  rclcpp_action::GoalResponse handle_goal(
      const rclcpp_action::GoalUUID &uuid,
      std::shared_ptr<const robot_msgs::action::Screw::Goal> goal);
  rclcpp_action::CancelResponse handle_cancel(
      const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle);
  void handle_accepted(
      const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle);
  void execute(
      const std::shared_ptr<rclcpp_action::ServerGoalHandle<robot_msgs::action::Screw>> goal_handle);
};

} // namespace screw_control

