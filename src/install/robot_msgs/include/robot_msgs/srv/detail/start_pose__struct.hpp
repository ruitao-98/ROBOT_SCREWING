// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_msgs:srv/StartPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_HPP_
#define ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_msgs__srv__StartPose_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__srv__StartPose_Request __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartPose_Request_
{
  using Type = StartPose_Request_<ContainerAllocator>;

  explicit StartPose_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit StartPose_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::srv::StartPose_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::srv::StartPose_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::srv::StartPose_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::srv::StartPose_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__srv__StartPose_Request
    std::shared_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__srv__StartPose_Request
    std::shared_ptr<robot_msgs::srv::StartPose_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartPose_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartPose_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartPose_Request_

// alias to use template instance with default allocator
using StartPose_Request =
  robot_msgs::srv::StartPose_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_msgs


#ifndef _WIN32
# define DEPRECATED__robot_msgs__srv__StartPose_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_msgs__srv__StartPose_Response __declspec(deprecated)
#endif

namespace robot_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StartPose_Response_
{
  using Type = StartPose_Response_<ContainerAllocator>;

  explicit StartPose_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos_para.begin(), this->pos_para.end(), 0.0);
      std::fill<typename std::array<double, 9>::iterator, double>(this->ori_para.begin(), this->ori_para.end(), 0.0);
    }
  }

  explicit StartPose_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc),
    pos_para(_alloc),
    ori_para(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
      std::fill<typename std::array<double, 3>::iterator, double>(this->pos_para.begin(), this->pos_para.end(), 0.0);
      std::fill<typename std::array<double, 9>::iterator, double>(this->ori_para.begin(), this->ori_para.end(), 0.0);
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _message_type message;
  using _pos_para_type =
    std::array<double, 3>;
  _pos_para_type pos_para;
  using _ori_para_type =
    std::array<double, 9>;
  _ori_para_type ori_para;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->message = _arg;
    return *this;
  }
  Type & set__pos_para(
    const std::array<double, 3> & _arg)
  {
    this->pos_para = _arg;
    return *this;
  }
  Type & set__ori_para(
    const std::array<double, 9> & _arg)
  {
    this->ori_para = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_msgs::srv::StartPose_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_msgs::srv::StartPose_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_msgs::srv::StartPose_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_msgs::srv::StartPose_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_msgs__srv__StartPose_Response
    std::shared_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_msgs__srv__StartPose_Response
    std::shared_ptr<robot_msgs::srv::StartPose_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StartPose_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    if (this->pos_para != other.pos_para) {
      return false;
    }
    if (this->ori_para != other.ori_para) {
      return false;
    }
    return true;
  }
  bool operator!=(const StartPose_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StartPose_Response_

// alias to use template instance with default allocator
using StartPose_Response =
  robot_msgs::srv::StartPose_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_msgs

namespace robot_msgs
{

namespace srv
{

struct StartPose
{
  using Request = robot_msgs::srv::StartPose_Request;
  using Response = robot_msgs::srv::StartPose_Response;
};

}  // namespace srv

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_HPP_
