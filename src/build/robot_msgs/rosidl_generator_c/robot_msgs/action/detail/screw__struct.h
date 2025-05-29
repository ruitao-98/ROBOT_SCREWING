// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_msgs:action/Screw.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__ACTION__DETAIL__SCREW__STRUCT_H_
#define ROBOT_MSGS__ACTION__DETAIL__SCREW__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_Goal
{
  int32_t num;
} robot_msgs__action__Screw_Goal;

// Struct for a sequence of robot_msgs__action__Screw_Goal.
typedef struct robot_msgs__action__Screw_Goal__Sequence
{
  robot_msgs__action__Screw_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_Goal__Sequence;


// Constants defined in the message

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_Result
{
  int32_t result;
} robot_msgs__action__Screw_Result;

// Struct for a sequence of robot_msgs__action__Screw_Result.
typedef struct robot_msgs__action__Screw_Result__Sequence
{
  robot_msgs__action__Screw_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_Result__Sequence;


// Constants defined in the message

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_Feedback
{
  double screw_status;
} robot_msgs__action__Screw_Feedback;

// Struct for a sequence of robot_msgs__action__Screw_Feedback.
typedef struct robot_msgs__action__Screw_Feedback__Sequence
{
  robot_msgs__action__Screw_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "robot_msgs/action/detail/screw__struct.h"

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  robot_msgs__action__Screw_Goal goal;
} robot_msgs__action__Screw_SendGoal_Request;

// Struct for a sequence of robot_msgs__action__Screw_SendGoal_Request.
typedef struct robot_msgs__action__Screw_SendGoal_Request__Sequence
{
  robot_msgs__action__Screw_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} robot_msgs__action__Screw_SendGoal_Response;

// Struct for a sequence of robot_msgs__action__Screw_SendGoal_Response.
typedef struct robot_msgs__action__Screw_SendGoal_Response__Sequence
{
  robot_msgs__action__Screw_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} robot_msgs__action__Screw_GetResult_Request;

// Struct for a sequence of robot_msgs__action__Screw_GetResult_Request.
typedef struct robot_msgs__action__Screw_GetResult_Request__Sequence
{
  robot_msgs__action__Screw_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_GetResult_Response
{
  int8_t status;
  robot_msgs__action__Screw_Result result;
} robot_msgs__action__Screw_GetResult_Response;

// Struct for a sequence of robot_msgs__action__Screw_GetResult_Response.
typedef struct robot_msgs__action__Screw_GetResult_Response__Sequence
{
  robot_msgs__action__Screw_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"

// Struct defined in action/Screw in the package robot_msgs.
typedef struct robot_msgs__action__Screw_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  robot_msgs__action__Screw_Feedback feedback;
} robot_msgs__action__Screw_FeedbackMessage;

// Struct for a sequence of robot_msgs__action__Screw_FeedbackMessage.
typedef struct robot_msgs__action__Screw_FeedbackMessage__Sequence
{
  robot_msgs__action__Screw_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_msgs__action__Screw_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_MSGS__ACTION__DETAIL__SCREW__STRUCT_H_
