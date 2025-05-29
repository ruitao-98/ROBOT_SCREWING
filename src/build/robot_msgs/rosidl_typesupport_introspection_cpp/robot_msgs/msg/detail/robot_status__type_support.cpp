// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robot_msgs/msg/detail/robot_status__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace robot_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void RobotStatus_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robot_msgs::msg::RobotStatus(_init);
}

void RobotStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robot_msgs::msg::RobotStatus *>(message_memory);
  typed_message->~RobotStatus();
}

size_t size_function__RobotStatus__ft_vector(const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * get_const_function__RobotStatus__ft_vector(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 6> *>(untyped_member);
  return &member[index];
}

void * get_function__RobotStatus__ft_vector(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 6> *>(untyped_member);
  return &member[index];
}

size_t size_function__RobotStatus__pos_vector(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__RobotStatus__pos_vector(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__RobotStatus__pos_vector(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__RobotStatus__rotation_matrix(const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * get_const_function__RobotStatus__rotation_matrix(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 9> *>(untyped_member);
  return &member[index];
}

void * get_function__RobotStatus__rotation_matrix(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 9> *>(untyped_member);
  return &member[index];
}

size_t size_function__RobotStatus__vel_vector(const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * get_const_function__RobotStatus__vel_vector(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 6> *>(untyped_member);
  return &member[index];
}

void * get_function__RobotStatus__vel_vector(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 6> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RobotStatus_message_member_array[4] = {
  {
    "ft_vector",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RobotStatus, ft_vector),  // bytes offset in struct
    nullptr,  // default value
    size_function__RobotStatus__ft_vector,  // size() function pointer
    get_const_function__RobotStatus__ft_vector,  // get_const(index) function pointer
    get_function__RobotStatus__ft_vector,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pos_vector",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RobotStatus, pos_vector),  // bytes offset in struct
    nullptr,  // default value
    size_function__RobotStatus__pos_vector,  // size() function pointer
    get_const_function__RobotStatus__pos_vector,  // get_const(index) function pointer
    get_function__RobotStatus__pos_vector,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "rotation_matrix",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RobotStatus, rotation_matrix),  // bytes offset in struct
    nullptr,  // default value
    size_function__RobotStatus__rotation_matrix,  // size() function pointer
    get_const_function__RobotStatus__rotation_matrix,  // get_const(index) function pointer
    get_function__RobotStatus__rotation_matrix,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "vel_vector",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RobotStatus, vel_vector),  // bytes offset in struct
    nullptr,  // default value
    size_function__RobotStatus__vel_vector,  // size() function pointer
    get_const_function__RobotStatus__vel_vector,  // get_const(index) function pointer
    get_function__RobotStatus__vel_vector,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RobotStatus_message_members = {
  "robot_msgs::msg",  // message namespace
  "RobotStatus",  // message name
  4,  // number of fields
  sizeof(robot_msgs::msg::RobotStatus),
  RobotStatus_message_member_array,  // message members
  RobotStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  RobotStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RobotStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RobotStatus_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace robot_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<robot_msgs::msg::RobotStatus>()
{
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::RobotStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, msg, RobotStatus)() {
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::RobotStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
