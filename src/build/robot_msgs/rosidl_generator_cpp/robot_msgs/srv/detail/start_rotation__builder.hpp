// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:srv/StartRotation.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__SRV__DETAIL__START_ROTATION__BUILDER_HPP_
#define ROBOT_MSGS__SRV__DETAIL__START_ROTATION__BUILDER_HPP_

#include "robot_msgs/srv/detail/start_rotation__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::srv::StartRotation_Request>()
{
  return ::robot_msgs::srv::StartRotation_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace robot_msgs


namespace robot_msgs
{

namespace srv
{

namespace builder
{

class Init_StartRotation_Response_ori_para
{
public:
  explicit Init_StartRotation_Response_ori_para(::robot_msgs::srv::StartRotation_Response & msg)
  : msg_(msg)
  {}
  ::robot_msgs::srv::StartRotation_Response ori_para(::robot_msgs::srv::StartRotation_Response::_ori_para_type arg)
  {
    msg_.ori_para = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

class Init_StartRotation_Response_pos_para
{
public:
  explicit Init_StartRotation_Response_pos_para(::robot_msgs::srv::StartRotation_Response & msg)
  : msg_(msg)
  {}
  Init_StartRotation_Response_ori_para pos_para(::robot_msgs::srv::StartRotation_Response::_pos_para_type arg)
  {
    msg_.pos_para = std::move(arg);
    return Init_StartRotation_Response_ori_para(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

class Init_StartRotation_Response_screw_pitch
{
public:
  explicit Init_StartRotation_Response_screw_pitch(::robot_msgs::srv::StartRotation_Response & msg)
  : msg_(msg)
  {}
  Init_StartRotation_Response_pos_para screw_pitch(::robot_msgs::srv::StartRotation_Response::_screw_pitch_type arg)
  {
    msg_.screw_pitch = std::move(arg);
    return Init_StartRotation_Response_pos_para(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

class Init_StartRotation_Response_rotation_speed
{
public:
  explicit Init_StartRotation_Response_rotation_speed(::robot_msgs::srv::StartRotation_Response & msg)
  : msg_(msg)
  {}
  Init_StartRotation_Response_screw_pitch rotation_speed(::robot_msgs::srv::StartRotation_Response::_rotation_speed_type arg)
  {
    msg_.rotation_speed = std::move(arg);
    return Init_StartRotation_Response_screw_pitch(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

class Init_StartRotation_Response_message
{
public:
  explicit Init_StartRotation_Response_message(::robot_msgs::srv::StartRotation_Response & msg)
  : msg_(msg)
  {}
  Init_StartRotation_Response_rotation_speed message(::robot_msgs::srv::StartRotation_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_StartRotation_Response_rotation_speed(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

class Init_StartRotation_Response_success
{
public:
  Init_StartRotation_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StartRotation_Response_message success(::robot_msgs::srv::StartRotation_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_StartRotation_Response_message(msg_);
  }

private:
  ::robot_msgs::srv::StartRotation_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::srv::StartRotation_Response>()
{
  return robot_msgs::srv::builder::Init_StartRotation_Response_success();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__SRV__DETAIL__START_ROTATION__BUILDER_HPP_
