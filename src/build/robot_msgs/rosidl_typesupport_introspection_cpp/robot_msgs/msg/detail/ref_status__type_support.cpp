// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robot_msgs/msg/detail/ref_status__struct.hpp"
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

void RefStatus_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robot_msgs::msg::RefStatus(_init);
}

void RefStatus_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robot_msgs::msg::RefStatus *>(message_memory);
  typed_message->~RefStatus();
}

size_t size_function__RefStatus__ref_pose(const void * untyped_member)
{
  (void)untyped_member;
  return 7;
}

const void * get_const_function__RefStatus__ref_pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 7> *>(untyped_member);
  return &member[index];
}

void * get_function__RefStatus__ref_pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 7> *>(untyped_member);
  return &member[index];
}

size_t size_function__RefStatus__ref_vel(const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * get_const_function__RefStatus__ref_vel(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 6> *>(untyped_member);
  return &member[index];
}

void * get_function__RefStatus__ref_vel(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 6> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember RefStatus_message_member_array[4] = {
  {
    "ref_pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    7,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RefStatus, ref_pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__RefStatus__ref_pose,  // size() function pointer
    get_const_function__RefStatus__ref_pose,  // get_const(index) function pointer
    get_function__RefStatus__ref_pose,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ref_vel",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RefStatus, ref_vel),  // bytes offset in struct
    nullptr,  // default value
    size_function__RefStatus__ref_vel,  // size() function pointer
    get_const_function__RefStatus__ref_vel,  // get_const(index) function pointer
    get_function__RefStatus__ref_vel,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RefStatus, timestamp),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "stop",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::RefStatus, stop),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers RefStatus_message_members = {
  "robot_msgs::msg",  // message namespace
  "RefStatus",  // message name
  4,  // number of fields
  sizeof(robot_msgs::msg::RefStatus),
  RefStatus_message_member_array,  // message members
  RefStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  RefStatus_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t RefStatus_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &RefStatus_message_members,
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
get_message_type_support_handle<robot_msgs::msg::RefStatus>()
{
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::RefStatus_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, msg, RefStatus)() {
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::RefStatus_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
