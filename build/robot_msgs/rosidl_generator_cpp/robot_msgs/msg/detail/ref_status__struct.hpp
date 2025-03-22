// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_HPP_
#define ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__msg__RefStatus __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__msg__RefStatus __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RefStatus_
{
  using Type = RefStatus_<ContainerAllocator>;

  explicit RefStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 7>::iterator, double>(this->ref_pose.begin(), this->ref_pose.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->ref_vel.begin(), this->ref_vel.end(), 0.0);
      this->timestamp = 0.0;
      this->stop = 0l;
    }
  }

  explicit RefStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ref_pose(_alloc),
    ref_vel(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<double, 7>::iterator, double>(this->ref_pose.begin(), this->ref_pose.end(), 0.0);
      std::fill<typename std::array<double, 6>::iterator, double>(this->ref_vel.begin(), this->ref_vel.end(), 0.0);
      this->timestamp = 0.0;
      this->stop = 0l;
    }
  }

  // field types and members
  using _ref_pose_type =
    std::array<double, 7>;
  _ref_pose_type ref_pose;
  using _ref_vel_type =
    std::array<double, 6>;
  _ref_vel_type ref_vel;
  using _timestamp_type =
    double;
  _timestamp_type timestamp;
  using _stop_type =
    int32_t;
  _stop_type stop;

  // setters for named parameter idiom
  Type & set__ref_pose(
    const std::array<double, 7> & _arg)
  {
    this->ref_pose = _arg;
    return *this;
  }
  Type & set__ref_vel(
    const std::array<double, 6> & _arg)
  {
    this->ref_vel = _arg;
    return *this;
  }
  Type & set__timestamp(
    const double & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__stop(
    const int32_t & _arg)
  {
    this->stop = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::msg::RefStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::msg::RefStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::RefStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::msg::RefStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__msg__RefStatus
    std::shared_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__msg__RefStatus
    std::shared_ptr<robot_msgs::msg::RefStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RefStatus_ & other) const
  {
    if (this->ref_pose != other.ref_pose) {
      return false;
    }
    if (this->ref_vel != other.ref_vel) {
      return false;
    }
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->stop != other.stop) {
      return false;
    }
    return true;
  }
  bool operator!=(const RefStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RefStatus_

// alias to use template instance with default allocator
using RefStatus =
  robot_msgs::msg::RefStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_HPP_
