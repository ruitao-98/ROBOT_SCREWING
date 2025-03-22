// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ControlCommand in the package robot_msgs.
typedef struct robot_msgs__msg__ControlCommand
{
  double k[6];
  double d[6];
} robot_msgs__msg__ControlCommand;

// Struct for a sequence of robot_msgs__msg__ControlCommand.
typedef struct robot_msgs__msg__ControlCommand__Sequence
{
  robot_msgs__msg__ControlCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__ControlCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__CONTROL_COMMAND__STRUCT_H_
