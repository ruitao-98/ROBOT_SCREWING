// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_

#include "robot_msgs/msg/detail/robot_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotStatus_vel_vector
{
public:
  explicit Init_RobotStatus_vel_vector(::robot_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::RobotStatus vel_vector(::robot_msgs::msg::RobotStatus::_vel_vector_type arg)
  {
    msg_.vel_vector = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_rotation_matrix
{
public:
  explicit Init_RobotStatus_rotation_matrix(::robot_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_vel_vector rotation_matrix(::robot_msgs::msg::RobotStatus::_rotation_matrix_type arg)
  {
    msg_.rotation_matrix = std::move(arg);
    return Init_RobotStatus_vel_vector(msg_);
  }

private:
  ::robot_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_pos_vector
{
public:
  explicit Init_RobotStatus_pos_vector(::robot_msgs::msg::RobotStatus & msg)
  : msg_(msg)
  {}
  Init_RobotStatus_rotation_matrix pos_vector(::robot_msgs::msg::RobotStatus::_pos_vector_type arg)
  {
    msg_.pos_vector = std::move(arg);
    return Init_RobotStatus_rotation_matrix(msg_);
  }

private:
  ::robot_msgs::msg::RobotStatus msg_;
};

class Init_RobotStatus_ft_vector
{
public:
  Init_RobotStatus_ft_vector()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotStatus_pos_vector ft_vector(::robot_msgs::msg::RobotStatus::_ft_vector_type arg)
  {
    msg_.ft_vector = std::move(arg);
    return Init_RobotStatus_pos_vector(msg_);
  }

private:
  ::robot_msgs::msg::RobotStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::RobotStatus>()
{
  return robot_msgs::msg::builder::Init_RobotStatus_ft_vector();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__BUILDER_HPP_
