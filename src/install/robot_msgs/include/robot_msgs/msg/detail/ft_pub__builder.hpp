// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/FtPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__FT_PUB__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__FT_PUB__BUILDER_HPP_

#include "robot_msgs/msg/detail/ft_pub__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_FtPub_tz
{
public:
  explicit Init_FtPub_tz(::robot_msgs::msg::FtPub & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::FtPub tz(::robot_msgs::msg::FtPub::_tz_type arg)
  {
    msg_.tz = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

class Init_FtPub_ty
{
public:
  explicit Init_FtPub_ty(::robot_msgs::msg::FtPub & msg)
  : msg_(msg)
  {}
  Init_FtPub_tz ty(::robot_msgs::msg::FtPub::_ty_type arg)
  {
    msg_.ty = std::move(arg);
    return Init_FtPub_tz(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

class Init_FtPub_tx
{
public:
  explicit Init_FtPub_tx(::robot_msgs::msg::FtPub & msg)
  : msg_(msg)
  {}
  Init_FtPub_ty tx(::robot_msgs::msg::FtPub::_tx_type arg)
  {
    msg_.tx = std::move(arg);
    return Init_FtPub_ty(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

class Init_FtPub_fz
{
public:
  explicit Init_FtPub_fz(::robot_msgs::msg::FtPub & msg)
  : msg_(msg)
  {}
  Init_FtPub_tx fz(::robot_msgs::msg::FtPub::_fz_type arg)
  {
    msg_.fz = std::move(arg);
    return Init_FtPub_tx(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

class Init_FtPub_fy
{
public:
  explicit Init_FtPub_fy(::robot_msgs::msg::FtPub & msg)
  : msg_(msg)
  {}
  Init_FtPub_fz fy(::robot_msgs::msg::FtPub::_fy_type arg)
  {
    msg_.fy = std::move(arg);
    return Init_FtPub_fz(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

class Init_FtPub_fx
{
public:
  Init_FtPub_fx()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FtPub_fy fx(::robot_msgs::msg::FtPub::_fx_type arg)
  {
    msg_.fx = std::move(arg);
    return Init_FtPub_fy(msg_);
  }

private:
  ::robot_msgs::msg::FtPub msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::FtPub>()
{
  return robot_msgs::msg::builder::Init_FtPub_fx();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__FT_PUB__BUILDER_HPP_
