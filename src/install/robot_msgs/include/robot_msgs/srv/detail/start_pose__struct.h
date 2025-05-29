// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:srv/StartPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_H_
#define ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/StartPose in the package robot_msgs.
typedef struct robot_msgs__srv__StartPose_Request
{
  uint8_t structure_needs_at_least_one_member;
} robot_msgs__srv__StartPose_Request;

// Struct for a sequence of robot_msgs__srv__StartPose_Request.
typedef struct robot_msgs__srv__StartPose_Request__Sequence
{
  robot_msgs__srv__StartPose_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__srv__StartPose_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/StartPose in the package robot_msgs.
typedef struct robot_msgs__srv__StartPose_Response
{
  bool success;
  rosidl_runtime_c__String message;
  double pos_para[3];
  double ori_para[9];
} robot_msgs__srv__StartPose_Response;

// Struct for a sequence of robot_msgs__srv__StartPose_Response.
typedef struct robot_msgs__srv__StartPose_Response__Sequence
{
  robot_msgs__srv__StartPose_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__srv__StartPose_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__SRV__DETAIL__START_POSE__STRUCT_H_
