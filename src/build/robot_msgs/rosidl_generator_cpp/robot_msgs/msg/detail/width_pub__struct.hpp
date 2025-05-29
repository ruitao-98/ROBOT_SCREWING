// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/WidthPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__WidthPub __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__WidthPub __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WidthPub_
{
  using Type = WidthPub_<ContainerAllocator>;

  explicit WidthPub_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->width = 0.0;
    }
  }

  explicit WidthPub_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->width = 0.0;
    }
  }

  // field types and members
  using _width_type =
    double;
  _width_type width;

  // setters for named parameter idiom
  Type & set__width(
    const double & _arg)
  {
    this->width = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::WidthPub_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::WidthPub_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::WidthPub_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::WidthPub_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__WidthPub
    std::shared_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__WidthPub
    std::shared_ptr<robot_msgs::msg::WidthPub_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WidthPub_ & other) const
  {
    if (this->width != other.width) {
      return false;
    }
    return true;
  }
  bool operator!=(const WidthPub_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WidthPub_

// alias to use template instance with default allocator
using WidthPub =
  robot_msgs::msg::WidthPub_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__WIDTH_PUB__STRUCT_HPP_
