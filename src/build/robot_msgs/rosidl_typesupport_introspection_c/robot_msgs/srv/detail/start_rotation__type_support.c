// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_msgs:srv/StartRotation.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_msgs/srv/detail/start_rotation__rosidl_typesupport_introspection_c.h"
#include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_msgs/srv/detail/start_rotation__functions.h"
#include "robot_msgs/srv/detail/start_rotation__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__srv__StartRotation_Request__init(message_memory);
}

void StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_fini_function(void * message_memory)
{
  robot_msgs__srv__StartRotation_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_members = {
  "robot_msgs__srv",  // message namespace
  "StartRotation_Request",  // message name
  1,  // number of fields
  sizeof(robot_msgs__srv__StartRotation_Request),
  StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_member_array,  // message members
  StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_type_support_handle = {
  0,
  &StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Request)() {
  if (!StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_type_support_handle.typesupport_identifier) {
    StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &StartRotation_Request__rosidl_typesupport_introspection_c__StartRotation_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_msgs/srv/detail/start_rotation__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_msgs/srv/detail/start_rotation__functions.h"
// already included above
// #include "robot_msgs/srv/detail/start_rotation__struct.h"


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_msgs__srv__StartRotation_Response__init(message_memory);
}

void StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_fini_function(void * message_memory)
{
  robot_msgs__srv__StartRotation_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_member_array[6] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rotation_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, rotation_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "screw_pitch",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, screw_pitch),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pos_para",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, pos_para),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ori_para",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(robot_msgs__srv__StartRotation_Response, ori_para),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_members = {
  "robot_msgs__srv",  // message namespace
  "StartRotation_Response",  // message name
  6,  // number of fields
  sizeof(robot_msgs__srv__StartRotation_Response),
  StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_member_array,  // message members
  StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_type_support_handle = {
  0,
  &StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Response)() {
  if (!StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_type_support_handle.typesupport_identifier) {
    StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &StartRotation_Response__rosidl_typesupport_introspection_c__StartRotation_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_msgs/srv/detail/start_rotation__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_members = {
  "robot_msgs__srv",  // service namespace
  "StartRotation",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_Request_message_type_support_handle,
  NULL  // response message
  // robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_type_support_handle = {
  0,
  &robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation)() {
  if (!robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_type_support_handle.typesupport_identifier) {
    robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_msgs, srv, StartRotation_Response)()->data;
  }

  return &robot_msgs__srv__detail__start_rotation__rosidl_typesupport_introspection_c__StartRotation_service_type_support_handle;
}
