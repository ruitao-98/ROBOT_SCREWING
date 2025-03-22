// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/RefStatus in the package robot_msgs.
typedef struct robot_msgs__msg__RefStatus
{
  double ref_pose[7];
  double ref_vel[6];
  double timestamp;
  int32_t stop;
} robot_msgs__msg__RefStatus;

// Struct for a sequence of robot_msgs__msg__RefStatus.
typedef struct robot_msgs__msg__RefStatus__Sequence
{
  robot_msgs__msg__RefStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__RefStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__REF_STATUS__STRUCT_H_
