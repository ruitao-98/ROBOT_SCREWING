// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__RobotStatus __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__RobotStatus __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotStatus_
{
  using Type = RobotStatus_<ContainerAllocator>;

  explicit RobotStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 6>::iterator, double>(this->ft_vector.begin(), this->ft_vector.end(), 0.0);
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos_vector.begin(), this->pos_vector.end(), 0.0);
      std::fill<typename std::array<double, 9>::iterator, double>(this->rotation_matrix.begin(), this->rotation_matrix.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->vel_vector.begin(), this->vel_vector.end(), 0.0);
    }
  }

  explicit RobotStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ft_vector(_alloc),
    pos_vector(_alloc),
    rotation_matrix(_alloc),
    vel_vector(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 6>::iterator, double>(this->ft_vector.begin(), this->ft_vector.end(), 0.0);
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos_vector.begin(), this->pos_vector.end(), 0.0);
      std::fill<typename std::array<double, 9>::iterator, double>(this->rotation_matrix.begin(), this->rotation_matrix.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->vel_vector.begin(), this->vel_vector.end(), 0.0);
    }
  }

  // field types and members
  using _ft_vector_type =
    std::array<double, 6>;
  _ft_vector_type ft_vector;
  using _pos_vector_type =
    std::array<double, 3>;
  _pos_vector_type pos_vector;
  using _rotation_matrix_type =
    std::array<double, 9>;
  _rotation_matrix_type rotation_matrix;
  using _vel_vector_type =
    std::array<double, 6>;
  _vel_vector_type vel_vector;

  // setters for named parameter idiom
  Type & set__ft_vector(
    const std::array<double, 6> & _arg)
  {
    this->ft_vector = _arg;
    return *this;
  }
  Type & set__pos_vector(
    const std::array<double, 3> & _arg)
  {
    this->pos_vector = _arg;
    return *this;
  }
  Type & set__rotation_matrix(
    const std::array<double, 9> & _arg)
  {
    this->rotation_matrix = _arg;
    return *this;
  }
  Type & set__vel_vector(
    const std::array<double, 6> & _arg)
  {
    this->vel_vector = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::RobotStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::RobotStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::RobotStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::RobotStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__RobotStatus
    std::shared_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__RobotStatus
    std::shared_ptr<robot_msgs::msg::RobotStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotStatus_ & other) const
  {
    if (this->ft_vector != other.ft_vector) {
      return false;
    }
    if (this->pos_vector != other.pos_vector) {
      return false;
    }
    if (this->rotation_matrix != other.rotation_matrix) {
      return false;
    }
    if (this->vel_vector != other.vel_vector) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotStatus_

// alias to use template instance with default allocator
using RobotStatus =
  robot_msgs::msg::RobotStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_HPP_
