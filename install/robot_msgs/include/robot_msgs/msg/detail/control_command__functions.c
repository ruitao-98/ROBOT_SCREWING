// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_msgs:msg/ControlCommand.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/control_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
robot_msgs__msg__ControlCommand__init(robot_msgs__msg__ControlCommand * msg)
{
  if (!msg) {
    return false;
  }
  // k
  // d
  return true;
}

void
robot_msgs__msg__ControlCommand__fini(robot_msgs__msg__ControlCommand * msg)
{
  if (!msg) {
    return;
  }
  // k
  // d
}

bool
robot_msgs__msg__ControlCommand__are_equal(const robot_msgs__msg__ControlCommand * lhs, const robot_msgs__msg__ControlCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // k
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->k[i] != rhs->k[i]) {
      return false;
    }
  }
  // d
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->d[i] != rhs->d[i]) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__ControlCommand__copy(
  const robot_msgs__msg__ControlCommand * input,
  robot_msgs__msg__ControlCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // k
  for (size_t i = 0; i < 6; ++i) {
    output->k[i] = input->k[i];
  }
  // d
  for (size_t i = 0; i < 6; ++i) {
    output->d[i] = input->d[i];
  }
  return true;
}

robot_msgs__msg__ControlCommand *
robot_msgs__msg__ControlCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__ControlCommand * msg = (robot_msgs__msg__ControlCommand *)allocator.allocate(sizeof(robot_msgs__msg__ControlCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_msgs__msg__ControlCommand));
  bool success = robot_msgs__msg__ControlCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_msgs__msg__ControlCommand__destroy(robot_msgs__msg__ControlCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_msgs__msg__ControlCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_msgs__msg__ControlCommand__Sequence__init(robot_msgs__msg__ControlCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__ControlCommand * data = NULL;

  if (size) {
    data = (robot_msgs__msg__ControlCommand *)allocator.zero_allocate(size, sizeof(robot_msgs__msg__ControlCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_msgs__msg__ControlCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_msgs__msg__ControlCommand__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_msgs__msg__ControlCommand__Sequence__fini(robot_msgs__msg__ControlCommand__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_msgs__msg__ControlCommand__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_msgs__msg__ControlCommand__Sequence *
robot_msgs__msg__ControlCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__ControlCommand__Sequence * array = (robot_msgs__msg__ControlCommand__Sequence *)allocator.allocate(sizeof(robot_msgs__msg__ControlCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_msgs__msg__ControlCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_msgs__msg__ControlCommand__Sequence__destroy(robot_msgs__msg__ControlCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_msgs__msg__ControlCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_msgs__msg__ControlCommand__Sequence__are_equal(const robot_msgs__msg__ControlCommand__Sequence * lhs, const robot_msgs__msg__ControlCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_msgs__msg__ControlCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__ControlCommand__Sequence__copy(
  const robot_msgs__msg__ControlCommand__Sequence * input,
  robot_msgs__msg__ControlCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_msgs__msg__ControlCommand);
    robot_msgs__msg__ControlCommand * data =
      (robot_msgs__msg__ControlCommand *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_msgs__msg__ControlCommand__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          robot_msgs__msg__ControlCommand__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_msgs__msg__ControlCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
