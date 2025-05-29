// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/FtPub.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/FtPub in the package robot_msgs.
typedef struct robot_msgs__msg__FtPub
{
  float fx;
  float fy;
  float fz;
  float tx;
  float ty;
  float tz;
} robot_msgs__msg__FtPub;

// Struct for a sequence of robot_msgs__msg__FtPub.
typedef struct robot_msgs__msg__FtPub__Sequence
{
  robot_msgs__msg__FtPub * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__FtPub__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__FT_PUB__STRUCT_H_
