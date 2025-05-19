// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/WidthPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__BUILDER_HPP_

#include "robot_msgs/msg/detail/width_pub__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_WidthPub_width
{
public:
  Init_WidthPub_width()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_msgs::msg::WidthPub width(::robot_msgs::msg::WidthPub::_width_type arg)
  {
    msg_.width = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::WidthPub msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::WidthPub>()
{
  return robot_msgs::msg::builder::Init_WidthPub_width();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__BUILDER_HPP_
