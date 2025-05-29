// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from robot_msgs:msg/FtPub.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/ft_pub__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "robot_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "robot_msgs/msg/detail/ft_pub__struct.h"
#include "robot_msgs/msg/detail/ft_pub__functions.h"
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


using _FtPub__ros_msg_type = robot_msgs__msg__FtPub;

static bool _FtPub__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _FtPub__ros_msg_type * ros_message = static_cast<const _FtPub__ros_msg_type *>(untyped_ros_message);
  // Field name: fx
  {
    cdr << ros_message->fx;
  }

  // Field name: fy
  {
    cdr << ros_message->fy;
  }

  // Field name: fz
  {
    cdr << ros_message->fz;
  }

  // Field name: tx
  {
    cdr << ros_message->tx;
  }

  // Field name: ty
  {
    cdr << ros_message->ty;
  }

  // Field name: tz
  {
    cdr << ros_message->tz;
  }

  return true;
}

static bool _FtPub__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _FtPub__ros_msg_type * ros_message = static_cast<_FtPub__ros_msg_type *>(untyped_ros_message);
  // Field name: fx
  {
    cdr >> ros_message->fx;
  }

  // Field name: fy
  {
    cdr >> ros_message->fy;
  }

  // Field name: fz
  {
    cdr >> ros_message->fz;
  }

  // Field name: tx
  {
    cdr >> ros_message->tx;
  }

  // Field name: ty
  {
    cdr >> ros_message->ty;
  }

  // Field name: tz
  {
    cdr >> ros_message->tz;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t get_serialized_size_robot_msgs__msg__FtPub(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _FtPub__ros_msg_type * ros_message = static_cast<const _FtPub__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name fx
  {
    size_t item_size = sizeof(ros_message->fx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fy
  {
    size_t item_size = sizeof(ros_message->fy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name fz
  {
    size_t item_size = sizeof(ros_message->fz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tx
  {
    size_t item_size = sizeof(ros_message->tx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ty
  {
    size_t item_size = sizeof(ros_message->ty);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tz
  {
    size_t item_size = sizeof(ros_message->tz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _FtPub__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_robot_msgs__msg__FtPub(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_robot_msgs
size_t max_serialized_size_robot_msgs__msg__FtPub(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: fx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: fz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: tx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ty
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: tz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _FtPub__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_robot_msgs__msg__FtPub(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_FtPub = {
  "robot_msgs::msg",
  "FtPub",
  _FtPub__cdr_serialize,
  _FtPub__cdr_deserialize,
  _FtPub__get_serialized_size,
  _FtPub__max_serialized_size
};

static rosidl_message_type_support_t _FtPub__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_FtPub,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, robot_msgs, msg, FtPub)() {
  return &_FtPub__type_support;
}

#if defined(__cplusplus)
}
#endif
