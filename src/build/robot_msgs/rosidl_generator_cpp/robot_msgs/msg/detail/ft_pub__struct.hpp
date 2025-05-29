// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/FtPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__FtPub __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__FtPub __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FtPub_
{
  using Type = FtPub_<ContainerAllocator>;

  explicit FtPub_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fx = 0.0f;
      this->fy = 0.0f;
      this->fz = 0.0f;
      this->tx = 0.0f;
      this->ty = 0.0f;
      this->tz = 0.0f;
    }
  }

  explicit FtPub_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fx = 0.0f;
      this->fy = 0.0f;
      this->fz = 0.0f;
      this->tx = 0.0f;
      this->ty = 0.0f;
      this->tz = 0.0f;
    }
  }

  // field types and members
  using _fx_type =
    float;
  _fx_type fx;
  using _fy_type =
    float;
  _fy_type fy;
  using _fz_type =
    float;
  _fz_type fz;
  using _tx_type =
    float;
  _tx_type tx;
  using _ty_type =
    float;
  _ty_type ty;
  using _tz_type =
    float;
  _tz_type tz;

  // setters for named parameter idiom
  Type & set__fx(
    const float & _arg)
  {
    this->fx = _arg;
    return *this;
  }
  Type & set__fy(
    const float & _arg)
  {
    this->fy = _arg;
    return *this;
  }
  Type & set__fz(
    const float & _arg)
  {
    this->fz = _arg;
    return *this;
  }
  Type & set__tx(
    const float & _arg)
  {
    this->tx = _arg;
    return *this;
  }
  Type & set__ty(
    const float & _arg)
  {
    this->ty = _arg;
    return *this;
  }
  Type & set__tz(
    const float & _arg)
  {
    this->tz = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::FtPub_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::FtPub_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::FtPub_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::FtPub_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::FtPub_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::FtPub_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::FtPub_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::FtPub_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::FtPub_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::FtPub_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__FtPub
    std::shared_ptr<robot_msgs::msg::FtPub_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__FtPub
    std::shared_ptr<robot_msgs::msg::FtPub_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FtPub_ & other) const
  {
    if (this->fx != other.fx) {
      return false;
    }
    if (this->fy != other.fy) {
      return false;
    }
    if (this->fz != other.fz) {
      return false;
    }
    if (this->tx != other.tx) {
      return false;
    }
    if (this->ty != other.ty) {
      return false;
    }
    if (this->tz != other.tz) {
      return false;
    }
    return true;
  }
  bool operator!=(const FtPub_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FtPub_

// alias to use template instance with default allocator
using FtPub =
  robot_msgs::msg::FtPub_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_HPP_
