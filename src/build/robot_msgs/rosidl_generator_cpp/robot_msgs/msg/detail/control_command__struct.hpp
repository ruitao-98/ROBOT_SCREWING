// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__ControlCommand __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__ControlCommand __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlCommand_
{
  using Type = ControlCommand_<ContainerAllocator>;

  explicit ControlCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 6>::iterator, double>(this->k.begin(), this->k.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->d.begin(), this->d.end(), 0.0);
    }
  }

  explicit ControlCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : k(_alloc),
    d(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 6>::iterator, double>(this->k.begin(), this->k.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->d.begin(), this->d.end(), 0.0);
    }
  }

  // field types and members
  using _k_type =
    std::array<double, 6>;
  _k_type k;
  using _d_type =
    std::array<double, 6>;
  _d_type d;

  // setters for named parameter idiom
  Type & set__k(
    const std::array<double, 6> & _arg)
  {
    this->k = _arg;
    return *this;
  }
  Type & set__d(
    const std::array<double, 6> & _arg)
  {
    this->d = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::ControlCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::ControlCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::ControlCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::ControlCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__ControlCommand
    std::shared_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__ControlCommand
    std::shared_ptr<robot_msgs::msg::ControlCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlCommand_ & other) const
  {
    if (this->k != other.k) {
      return false;
    }
    if (this->d != other.d) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlCommand_

// alias to use template instance with default allocator
using ControlCommand =
  robot_msgs::msg::ControlCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_HPP_
