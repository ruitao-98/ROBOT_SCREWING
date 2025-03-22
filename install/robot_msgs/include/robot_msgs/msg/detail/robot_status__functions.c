// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_msgs:msg/RobotStatus.idl
// generated code does not contain a copyright notice
#include "robot_msgs/msg/detail/robot_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
robot_msgs__msg__RobotStatus__init(robot_msgs__msg__RobotStatus * msg)
{
  if (!msg) {
    return false;
  }
  // ft_vector
  // pos_vector
  // rotation_matrix
  // vel_vector
  return true;
}

void
robot_msgs__msg__RobotStatus__fini(robot_msgs__msg__RobotStatus * msg)
{
  if (!msg) {
    return;
  }
  // ft_vector
  // pos_vector
  // rotation_matrix
  // vel_vector
}

bool
robot_msgs__msg__RobotStatus__are_equal(const robot_msgs__msg__RobotStatus * lhs, const robot_msgs__msg__RobotStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ft_vector
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->ft_vector[i] != rhs->ft_vector[i]) {
      return false;
    }
  }
  // pos_vector
  for (size_t i = 0; i < 3; ++i) {
    if (lhs->pos_vector[i] != rhs->pos_vector[i]) {
      return false;
    }
  }
  // rotation_matrix
  for (size_t i = 0; i < 9; ++i) {
    if (lhs->rotation_matrix[i] != rhs->rotation_matrix[i]) {
      return false;
    }
  }
  // vel_vector
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->vel_vector[i] != rhs->vel_vector[i]) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__RobotStatus__copy(
  const robot_msgs__msg__RobotStatus * input,
  robot_msgs__msg__RobotStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // ft_vector
  for (size_t i = 0; i < 6; ++i) {
    output->ft_vector[i] = input->ft_vector[i];
  }
  // pos_vector
  for (size_t i = 0; i < 3; ++i) {
    output->pos_vector[i] = input->pos_vector[i];
  }
  // rotation_matrix
  for (size_t i = 0; i < 9; ++i) {
    output->rotation_matrix[i] = input->rotation_matrix[i];
  }
  // vel_vector
  for (size_t i = 0; i < 6; ++i) {
    output->vel_vector[i] = input->vel_vector[i];
  }
  return true;
}

robot_msgs__msg__RobotStatus *
robot_msgs__msg__RobotStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotStatus * msg = (robot_msgs__msg__RobotStatus *)allocator.allocate(sizeof(robot_msgs__msg__RobotStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_msgs__msg__RobotStatus));
  bool success = robot_msgs__msg__RobotStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_msgs__msg__RobotStatus__destroy(robot_msgs__msg__RobotStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_msgs__msg__RobotStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_msgs__msg__RobotStatus__Sequence__init(robot_msgs__msg__RobotStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotStatus * data = NULL;

  if (size) {
    data = (robot_msgs__msg__RobotStatus *)allocator.zero_allocate(size, sizeof(robot_msgs__msg__RobotStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_msgs__msg__RobotStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_msgs__msg__RobotStatus__fini(&data[i - 1]);
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
robot_msgs__msg__RobotStatus__Sequence__fini(robot_msgs__msg__RobotStatus__Sequence * array)
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
      robot_msgs__msg__RobotStatus__fini(&array->data[i]);
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

robot_msgs__msg__RobotStatus__Sequence *
robot_msgs__msg__RobotStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_msgs__msg__RobotStatus__Sequence * array = (robot_msgs__msg__RobotStatus__Sequence *)allocator.allocate(sizeof(robot_msgs__msg__RobotStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_msgs__msg__RobotStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_msgs__msg__RobotStatus__Sequence__destroy(robot_msgs__msg__RobotStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_msgs__msg__RobotStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_msgs__msg__RobotStatus__Sequence__are_equal(const robot_msgs__msg__RobotStatus__Sequence * lhs, const robot_msgs__msg__RobotStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_msgs__msg__RobotStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_msgs__msg__RobotStatus__Sequence__copy(
  const robot_msgs__msg__RobotStatus__Sequence * input,
  robot_msgs__msg__RobotStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_msgs__msg__RobotStatus);
    robot_msgs__msg__RobotStatus * data =
      (robot_msgs__msg__RobotStatus *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_msgs__msg__RobotStatus__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          robot_msgs__msg__RobotStatus__fini(&data[i]);
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
    if (!robot_msgs__msg__RobotStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
