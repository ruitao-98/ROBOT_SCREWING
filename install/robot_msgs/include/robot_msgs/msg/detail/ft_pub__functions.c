// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_msgs:msg/FtPub.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/ft_pub__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
robot_msgs__msg__FtPub__init(robot_msgs__msg__FtPub * msg)
{
  if (!msg) {
    return false;
  }
  // fx
  // fy
  // fz
  // tx
  // ty
  // tz
  return true;
}

void
robot_msgs__msg__FtPub__fini(robot_msgs__msg__FtPub * msg)
{
  if (!msg) {
    return;
  }
  // fx
  // fy
  // fz
  // tx
  // ty
  // tz
}

bool
robot_msgs__msg__FtPub__are_equal(const robot_msgs__msg__FtPub * lhs, const robot_msgs__msg__FtPub * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // fx
  if (lhs->fx != rhs->fx) {
    return false;
  }
  // fy
  if (lhs->fy != rhs->fy) {
    return false;
  }
  // fz
  if (lhs->fz != rhs->fz) {
    return false;
  }
  // tx
  if (lhs->tx != rhs->tx) {
    return false;
  }
  // ty
  if (lhs->ty != rhs->ty) {
    return false;
  }
  // tz
  if (lhs->tz != rhs->tz) {
    return false;
  }
  return true;
}

bool
robot_msgs__msg__FtPub__copy(
  const robot_msgs__msg__FtPub * input,
  robot_msgs__msg__FtPub * output)
{
  if (!input || !output) {
    return false;
  }
  // fx
  output->fx = input->fx;
  // fy
  output->fy = input->fy;
  // fz
  output->fz = input->fz;
  // tx
  output->tx = input->tx;
  // ty
  output->ty = input->ty;
  // tz
  output->tz = input->tz;
  return true;
}

robot_msgs__msg__FtPub *
robot_msgs__msg__FtPub__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__FtPub * msg = (robot_msgs__msg__FtPub *)allocator.allocate(sizeof(robot_msgs__msg__FtPub), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_msgs__msg__FtPub));
  bool success = robot_msgs__msg__FtPub__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_msgs__msg__FtPub__destroy(robot_msgs__msg__FtPub * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_msgs__msg__FtPub__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_msgs__msg__FtPub__Sequence__init(robot_msgs__msg__FtPub__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__FtPub * data = NULL;

  if (size) {
    data = (robot_msgs__msg__FtPub *)allocator.zero_allocate(size, sizeof(robot_msgs__msg__FtPub), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_msgs__msg__FtPub__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_msgs__msg__FtPub__fini(&data[i - 1]);
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
robot_msgs__msg__FtPub__Sequence__fini(robot_msgs__msg__FtPub__Sequence * array)
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
      robot_msgs__msg__FtPub__fini(&array->data[i]);
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

robot_msgs__msg__FtPub__Sequence *
robot_msgs__msg__FtPub__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__FtPub__Sequence * array = (robot_msgs__msg__FtPub__Sequence *)allocator.allocate(sizeof(robot_msgs__msg__FtPub__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_msgs__msg__FtPub__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_msgs__msg__FtPub__Sequence__destroy(robot_msgs__msg__FtPub__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_msgs__msg__FtPub__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_msgs__msg__FtPub__Sequence__are_equal(const robot_msgs__msg__FtPub__Sequence * lhs, const robot_msgs__msg__FtPub__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_msgs__msg__FtPub__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__FtPub__Sequence__copy(
  const robot_msgs__msg__FtPub__Sequence * input,
  robot_msgs__msg__FtPub__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_msgs__msg__FtPub);
    robot_msgs__msg__FtPub * data =
      (robot_msgs__msg__FtPub *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_msgs__msg__FtPub__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          robot_msgs__msg__FtPub__fini(&data[i]);
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
    if (!robot_msgs__msg__FtPub__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
