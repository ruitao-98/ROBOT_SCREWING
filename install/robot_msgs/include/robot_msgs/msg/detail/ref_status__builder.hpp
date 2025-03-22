// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__REF_STATUS__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__REF_STATUS__BUILDER_HPP_

#include "robot_msgs/msg/detail/ref_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_RefStatus_stop
{
public:
  explicit Init_RefStatus_stop(::robot_msgs::msg::RefStatus & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::RefStatus stop(::robot_msgs::msg::RefStatus::_stop_type arg)
  {
    msg_.stop = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::RefStatus msg_;
};

class Init_RefStatus_timestamp
{
public:
  explicit Init_RefStatus_timestamp(::robot_msgs::msg::RefStatus & msg)
  : msg_(msg)
  {}
  Init_RefStatus_stop timestamp(::robot_msgs::msg::RefStatus::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_RefStatus_stop(msg_);
  }

private:
  ::robot_msgs::msg::RefStatus msg_;
};

class Init_RefStatus_ref_vel
{
public:
  explicit Init_RefStatus_ref_vel(::robot_msgs::msg::RefStatus & msg)
  : msg_(msg)
  {}
  Init_RefStatus_timestamp ref_vel(::robot_msgs::msg::RefStatus::_ref_vel_type arg)
  {
    msg_.ref_vel = std::move(arg);
    return Init_RefStatus_timestamp(msg_);
  }

private:
  ::robot_msgs::msg::RefStatus msg_;
};

class Init_RefStatus_ref_pose
{
public:
  Init_RefStatus_ref_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RefStatus_ref_vel ref_pose(::robot_msgs::msg::RefStatus::_ref_pose_type arg)
  {
    msg_.ref_pose = std::move(arg);
    return Init_RefStatus_ref_vel(msg_);
  }

private:
  ::robot_msgs::msg::RefStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::RefStatus>()
{
  return robot_msgs::msg::builder::Init_RefStatus_ref_pose();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__REF_STATUS__BUILDER_HPP_
