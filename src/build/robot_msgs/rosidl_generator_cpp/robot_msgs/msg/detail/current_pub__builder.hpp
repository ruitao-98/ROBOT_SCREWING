// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/CurrentPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__CURRENT_PUB__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__CURRENT_PUB__BUILDER_HPP_

#include "robot_msgs/msg/detail/current_pub__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_CurrentPub_current
{
public:
  Init_CurrentPub_current()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::msg::CurrentPub current(::robot_msgs::msg::CurrentPub::_current_type arg)
  {
    msg_.current = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::CurrentPub msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::CurrentPub>()
{
  return robot_msgs::msg::builder::Init_CurrentPub_current();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__CURRENT_PUB__BUILDER_HPP_
