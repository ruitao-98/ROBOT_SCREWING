// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_msgs:action/Screw.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
#include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_msgs/action/detail/screw__functions.h"
#include "robot_msgs/action/detail/screw__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_Goal__init(message_memory);
}

void Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_Goal__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_member_array[1] = {
  {
    "num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_Goal, num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_Goal",  // message name
  1,  // number of fields
  sizeof(robot_msgs__action__Screw_Goal),
  Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_member_array,  // message members
  Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_type_support_handle = {
  0,
  &Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Goal)() {
  if (!Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_type_support_handle.typesupport_identifier) {
    Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_Goal__rosidl_typesupport_introspection_c__Screw_Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_Result__init(message_memory);
}

void Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_Result__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_member_array[1] = {
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_Result, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_Result",  // message name
  1,  // number of fields
  sizeof(robot_msgs__action__Screw_Result),
  Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_member_array,  // message members
  Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_type_support_handle = {
  0,
  &Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Result)() {
  if (!Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_type_support_handle.typesupport_identifier) {
    Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_Result__rosidl_typesupport_introspection_c__Screw_Result_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_Feedback__init(message_memory);
}

void Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_Feedback__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_member_array[1] = {
  {
    "screw_status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_Feedback, screw_status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_Feedback",  // message name
  1,  // number of fields
  sizeof(robot_msgs__action__Screw_Feedback),
  Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_member_array,  // message members
  Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_type_support_handle = {
  0,
  &Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Feedback)() {
  if (!Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_type_support_handle.typesupport_identifier) {
    Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_Feedback__rosidl_typesupport_introspection_c__Screw_Feedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `goal`
#include "robot_msgs/action/screw.h"
// Member `goal`
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_SendGoal_Request__init(message_memory);
}

void Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_SendGoal_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_SendGoal_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_SendGoal_Request, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_SendGoal_Request",  // message name
  2,  // number of fields
  sizeof(robot_msgs__action__Screw_SendGoal_Request),
  Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_member_array,  // message members
  Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_type_support_handle = {
  0,
  &Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Request)() {
  Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Goal)();
  if (!Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_type_support_handle.typesupport_identifier) {
    Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_SendGoal_Request__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_SendGoal_Response__init(message_memory);
}

void Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_SendGoal_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_member_array[2] = {
  {
    "accepted",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_SendGoal_Response, accepted),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_SendGoal_Response, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_SendGoal_Response",  // message name
  2,  // number of fields
  sizeof(robot_msgs__action__Screw_SendGoal_Response),
  Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_member_array,  // message members
  Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_type_support_handle = {
  0,
  &Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Response)() {
  Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_type_support_handle.typesupport_identifier) {
    Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_SendGoal_Response__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_members = {
  "robot_msgs__action",  // service namespace
  "Screw_SendGoal",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_Request_message_type_support_handle,
  NULL  // response message
  // robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_type_support_handle = {
  0,
  &robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal)() {
  if (!robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_type_support_handle.typesupport_identifier) {
    robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_SendGoal_Response)()->data;
  }

  return &robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_SendGoal_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_GetResult_Request__init(message_memory);
}

void Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_GetResult_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_member_array[1] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_GetResult_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_GetResult_Request",  // message name
  1,  // number of fields
  sizeof(robot_msgs__action__Screw_GetResult_Request),
  Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_member_array,  // message members
  Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_type_support_handle = {
  0,
  &Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Request)() {
  Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  if (!Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_type_support_handle.typesupport_identifier) {
    Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_GetResult_Request__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


// Include directives for member types
// Member `result`
// already included above
// #include "robot_msgs/action/screw.h"
// Member `result`
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_GetResult_Response__init(message_memory);
}

void Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_GetResult_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_GetResult_Response, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_GetResult_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_GetResult_Response",  // message name
  2,  // number of fields
  sizeof(robot_msgs__action__Screw_GetResult_Response),
  Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_member_array,  // message members
  Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_type_support_handle = {
  0,
  &Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Response)() {
  Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Result)();
  if (!Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_type_support_handle.typesupport_identifier) {
    Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_GetResult_Response__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_members = {
  "robot_msgs__action",  // service namespace
  "Screw_GetResult",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_Request_message_type_support_handle,
  NULL  // response message
  // robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_type_support_handle = {
  0,
  &robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult)() {
  if (!robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_type_support_handle.typesupport_identifier) {
    robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_GetResult_Response)()->data;
  }

  return &robot_msgs__action__detail__screw__rosidl_typesupport_introspection_c__Screw_GetResult_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/action/detail/screw__functions.h"
// already included above
// #include "robot_msgs/action/detail/screw__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__rosidl_typesupport_introspection_c.h"
// Member `feedback`
// already included above
// #include "robot_msgs/action/screw.h"
// Member `feedback`
// already included above
// #include "robot_msgs/action/detail/screw__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__action__Screw_FeedbackMessage__init(message_memory);
}

void Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_fini_function(void * message_memory)
{
  robot_msgs__action__Screw_FeedbackMessage__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_FeedbackMessage, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "feedback",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__action__Screw_FeedbackMessage, feedback),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_members = {
  "robot_msgs__action",  // message namespace
  "Screw_FeedbackMessage",  // message name
  2,  // number of fields
  sizeof(robot_msgs__action__Screw_FeedbackMessage),
  Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_member_array,  // message members
  Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_type_support_handle = {
  0,
  &Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_FeedbackMessage)() {
  Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, action, Screw_Feedback)();
  if (!Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_type_support_handle.typesupport_identifier) {
    Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Screw_FeedbackMessage__rosidl_typesupport_introspection_c__Screw_FeedbackMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
