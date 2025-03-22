// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_

#include "robot_msgs/msg/detail/control_command__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_ControlCommand_d
{
public:
  explicit Init_ControlCommand_d(::robot_msgs::msg::ControlCommand & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::ControlCommand d(::robot_msgs::msg::ControlCommand::_d_type arg)
  {
    msg_.d = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::ControlCommand msg_;
};

class Init_ControlCommand_k
{
public:
  Init_ControlCommand_k()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlCommand_d k(::robot_msgs::msg::ControlCommand::_k_type arg)
  {
    msg_.k = std::move(arg);
    return Init_ControlCommand_d(msg_);
  }

private:
  ::robot_msgs::msg::ControlCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::ControlCommand>()
{
  return robot_msgs::msg::builder::Init_ControlCommand_k();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__BUILDER_HPP_
