// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robot_msgs:msg/RefStatus.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/ref_status__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robot_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robot_msgs/msg/detail/ref_status__struct.h"
#include "robot_msgs/msg/detail/ref_status__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _RefStatus__ros_msg_type = robot_msgs__msg__RefStatus;

static bool _RefStatus__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RefStatus__ros_msg_type * ros_message = static_cast<const _RefStatus__ros_msg_type *>(untyped_ros_message);
  // Field name: ref_pose
  {
    size_t size = 7;
    auto array_ptr = ros_message->ref_pose;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: ref_vel
  {
    size_t size = 6;
    auto array_ptr = ros_message->ref_vel;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: stop
  {
    cdr << ros_message->stop;
  }

  return true;
}

static bool _RefStatus__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RefStatus__ros_msg_type * ros_message = static_cast<_RefStatus__ros_msg_type *>(untyped_ros_message);
  // Field name: ref_pose
  {
    size_t size = 7;
    auto array_ptr = ros_message->ref_pose;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: ref_vel
  {
    size_t size = 6;
    auto array_ptr = ros_message->ref_vel;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: stop
  {
    cdr >> ros_message->stop;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t get_serialized_size_robot_msgs__msg__RefStatus(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RefStatus__ros_msg_type * ros_message = static_cast<const _RefStatus__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ref_pose
  {
    size_t array_size = 7;
    auto array_ptr = ros_message->ref_pose;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ref_vel
  {
    size_t array_size = 6;
    auto array_ptr = ros_message->ref_vel;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name stop
  {
    size_t item_size = sizeof(ros_message->stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _RefStatus__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robot_msgs__msg__RefStatus(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t max_serialized_size_robot_msgs__msg__RefStatus(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: ref_pose
  {
    size_t array_size = 7;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ref_vel
  {
    size_t array_size = 6;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: timestamp
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: stop
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _RefStatus__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_robot_msgs__msg__RefStatus(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_RefStatus = {
  "robot_msgs::msg",
  "RefStatus",
  _RefStatus__cdr_serialize,
  _RefStatus__cdr_deserialize,
  _RefStatus__get_serialized_size,
  _RefStatus__max_serialized_size
};

static rosidl_message_type_support_t _RefStatus__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RefStatus,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robot_msgs, msg, RefStatus)() {
  return &_RefStatus__type_support;
}

#if defined(__cplusplus)
}
#endif
