// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
#define ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/RobotStatus in the package robot_msgs.
typedef struct robot_msgs__msg__RobotStatus
{
  double ft_vector[6];
  double pos_vector[3];
  double rotation_matrix[9];
  double vel_vector[6];
} robot_msgs__msg__RobotStatus;

// Struct for a sequence of robot_msgs__msg__RobotStatus.
typedef struct robot_msgs__msg__RobotStatus__Sequence
{
  robot_msgs__msg__RobotStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__msg__RobotStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__MSG__DETAIL__ROBOT_STATUS__STRUCT_H_
