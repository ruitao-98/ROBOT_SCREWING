// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from robot_msgs:msg/WidthPub.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "robot_msgs/msg/detail/width_pub__struct.hpp"
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

void WidthPub_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) robot_msgs::msg::WidthPub(_init);
}

void WidthPub_fini_function(void * message_memory)
{
  auto typed_message = static_cast<robot_msgs::msg::WidthPub *>(message_memory);
  typed_message->~WidthPub();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember WidthPub_message_member_array[1] = {
  {
    "width",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs::msg::WidthPub, width),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers WidthPub_message_members = {
  "robot_msgs::msg",  // message namespace
  "WidthPub",  // message name
  1,  // number of fields
  sizeof(robot_msgs::msg::WidthPub),
  WidthPub_message_member_array,  // message members
  WidthPub_init_function,  // function to initialize message memory (memory has to be allocated)
  WidthPub_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t WidthPub_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &WidthPub_message_members,
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
get_message_type_support_handle<robot_msgs::msg::WidthPub>()
{
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::WidthPub_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, robot_msgs, msg, WidthPub)() {
  return &::robot_msgs::msg::rosidl_typesupport_introspection_cpp::WidthPub_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
