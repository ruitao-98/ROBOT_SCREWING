// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_
#define ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_

#include "robot_msgs/msg/detail/robot_status__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_msgs::msg::RobotStatus>()
{
  return "robot_msgs::msg::RobotStatus";
}

template<>
inline const char * name<robot_msgs::msg::RobotStatus>()
{
  return "robot_msgs/msg/RobotStatus";
}

template<>
struct has_fixed_size<robot_msgs::msg::RobotStatus>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_msgs::msg::RobotStatus>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_msgs::msg::RobotStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__TRAITS_HPP_
