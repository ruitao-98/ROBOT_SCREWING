# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robot_msgs:msg/RefStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'ref_pose'
# Member 'ref_vel'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RefStatus(type):
    """Metaclass of message 'RefStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robot_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robot_msgs.msg.RefStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ref_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ref_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ref_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ref_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ref_status

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RefStatus(metaclass=Metaclass_RefStatus):
    """Message class 'RefStatus'."""

    __slots__ = [
        '_ref_pose',
        '_ref_vel',
        '_timestamp',
        '_stop',
    ]

    _fields_and_field_types = {
        'ref_pose': 'double[7]',
        'ref_vel': 'double[6]',
        'timestamp': 'double',
        'stop': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 7),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 6),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'ref_pose' not in kwargs:
            self.ref_pose = numpy.zeros(7, dtype=numpy.float64)
        else:
            self.ref_pose = numpy.array(kwargs.get('ref_pose'), dtype=numpy.float64)
            assert self.ref_pose.shape == (7, )
        if 'ref_vel' not in kwargs:
            self.ref_vel = numpy.zeros(6, dtype=numpy.float64)
        else:
            self.ref_vel = numpy.array(kwargs.get('ref_vel'), dtype=numpy.float64)
            assert self.ref_vel.shape == (6, )
        self.timestamp = kwargs.get('timestamp', float())
        self.stop = kwargs.get('stop', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if all(self.ref_pose != other.ref_pose):
            return False
        if all(self.ref_vel != other.ref_vel):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.stop != other.stop:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def ref_pose(self):
        """Message field 'ref_pose'."""
        return self._ref_pose

    @ref_pose.setter
    def ref_pose(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'ref_pose' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 7, \
                "The 'ref_pose' numpy.ndarray() must have a size of 7"
            self._ref_pose = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 7 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'ref_pose' field must be a set or sequence with length 7 and each value of type 'float'"
        self._ref_pose = numpy.array(value, dtype=numpy.float64)

    @property
    def ref_vel(self):
        """Message field 'ref_vel'."""
        return self._ref_vel

    @ref_vel.setter
    def ref_vel(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'ref_vel' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 6, \
                "The 'ref_vel' numpy.ndarray() must have a size of 6"
            self._ref_vel = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 6 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'ref_vel' field must be a set or sequence with length 6 and each value of type 'float'"
        self._ref_vel = numpy.array(value, dtype=numpy.float64)

    @property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'timestamp' field must be of type 'float'"
        self._timestamp = value

    @property
    def stop(self):
        """Message field 'stop'."""
        return self._stop

    @stop.setter
    def stop(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'stop' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'stop' field must be an integer in [-2147483648, 2147483647]"
        self._stop = value
