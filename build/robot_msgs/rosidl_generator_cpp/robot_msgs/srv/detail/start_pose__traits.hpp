// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_msgs:srv/StartPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__SRV__DETAIL__START_POSE__TRAITS_HPP_
#define ROBOT_MSGS__SRV__DETAIL__START_POSE__TRAITS_HPP_

#include "robot_msgs/srv/detail/start_pose__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_msgs::srv::StartPose_Request>()
{
  return "robot_msgs::srv::StartPose_Request";
}

template<>
inline const char * name<robot_msgs::srv::StartPose_Request>()
{
  return "robot_msgs/srv/StartPose_Request";
}

template<>
struct has_fixed_size<robot_msgs::srv::StartPose_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_msgs::srv::StartPose_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_msgs::srv::StartPose_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_msgs::srv::StartPose_Response>()
{
  return "robot_msgs::srv::StartPose_Response";
}

template<>
inline const char * name<robot_msgs::srv::StartPose_Response>()
{
  return "robot_msgs/srv/StartPose_Response";
}

template<>
struct has_fixed_size<robot_msgs::srv::StartPose_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_msgs::srv::StartPose_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_msgs::srv::StartPose_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_msgs::srv::StartPose>()
{
  return "robot_msgs::srv::StartPose";
}

template<>
inline const char * name<robot_msgs::srv::StartPose>()
{
  return "robot_msgs/srv/StartPose";
}

template<>
struct has_fixed_size<robot_msgs::srv::StartPose>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_msgs::srv::StartPose_Request>::value &&
    has_fixed_size<robot_msgs::srv::StartPose_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_msgs::srv::StartPose>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_msgs::srv::StartPose_Request>::value &&
    has_bounded_size<robot_msgs::srv::StartPose_Response>::value
  >
{
};

template<>
struct is_service<robot_msgs::srv::StartPose>
  : std::true_type
{
};

template<>
struct is_service_request<robot_msgs::srv::StartPose_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_msgs::srv::StartPose_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_MSGS__SRV__DETAIL__START_POSE__TRAITS_HPP_
