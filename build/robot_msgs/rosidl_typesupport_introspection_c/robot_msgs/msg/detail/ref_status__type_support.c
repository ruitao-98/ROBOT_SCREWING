// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_msgs/msg/detail/ref_status__rosidl_typesupport_introspection_c.h"
#include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_msgs/msg/detail/ref_status__functions.h"
#include "robot_msgs/msg/detail/ref_status__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void RefStatus__rosidl_typesupport_introspection_c__RefStatus_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__msg__RefStatus__init(message_memory);
}

void RefStatus__rosidl_typesupport_introspection_c__RefStatus_fini_function(void * message_memory)
{
  robot_msgs__msg__RefStatus__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_member_array[4] = {
  {
    "ref_pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    7,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__msg__RefStatus, ref_pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ref_vel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__msg__RefStatus, ref_vel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__msg__RefStatus, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stop",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__msg__RefStatus, stop),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_members = {
  "robot_msgs__msg",  // message namespace
  "RefStatus",  // message name
  4,  // number of fields
  sizeof(robot_msgs__msg__RefStatus),
  RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_member_array,  // message members
  RefStatus__rosidl_typesupport_introspection_c__RefStatus_init_function,  // function to initialize message memory (memory has to be allocated)
  RefStatus__rosidl_typesupport_introspection_c__RefStatus_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_type_support_handle = {
  0,
  &RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, msg, RefStatus)() {
  if (!RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_type_support_handle.typesupport_identifier) {
    RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &RefStatus__rosidl_typesupport_introspection_c__RefStatus_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
