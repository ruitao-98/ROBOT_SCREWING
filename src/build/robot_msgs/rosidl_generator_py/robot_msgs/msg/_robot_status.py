# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robot_msgs:msg/RobotStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'ft_vector'
# Member 'pos_vector'
# Member 'rotation_matrix'
# Member 'vel_vector'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RobotStatus(type):
    """Metaclass of message 'RobotStatus'."""

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
                'robot_msgs.msg.RobotStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__robot_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__robot_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__robot_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__robot_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__robot_status

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RobotStatus(metaclass=Metaclass_RobotStatus):
    """Message class 'RobotStatus'."""

    __slots__ = [
        '_ft_vector',
        '_pos_vector',
        '_rotation_matrix',
        '_vel_vector',
    ]

    _fields_and_field_types = {
        'ft_vector': 'double[6]',
        'pos_vector': 'double[3]',
        'rotation_matrix': 'double[9]',
        'vel_vector': 'double[6]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 6),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 9),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 6),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'ft_vector' not in kwargs:
            self.ft_vector = numpy.zeros(6, dtype=numpy.float64)
        else:
            self.ft_vector = numpy.array(kwargs.get('ft_vector'), dtype=numpy.float64)
            assert self.ft_vector.shape == (6, )
        if 'pos_vector' not in kwargs:
            self.pos_vector = numpy.zeros(3, dtype=numpy.float64)
        else:
            self.pos_vector = numpy.array(kwargs.get('pos_vector'), dtype=numpy.float64)
            assert self.pos_vector.shape == (3, )
        if 'rotation_matrix' not in kwargs:
            self.rotation_matrix = numpy.zeros(9, dtype=numpy.float64)
        else:
            self.rotation_matrix = numpy.array(kwargs.get('rotation_matrix'), dtype=numpy.float64)
            assert self.rotation_matrix.shape == (9, )
        if 'vel_vector' not in kwargs:
            self.vel_vector = numpy.zeros(6, dtype=numpy.float64)
        else:
            self.vel_vector = numpy.array(kwargs.get('vel_vector'), dtype=numpy.float64)
            assert self.vel_vector.shape == (6, )

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
        if all(self.ft_vector != other.ft_vector):
            return False
        if all(self.pos_vector != other.pos_vector):
            return False
        if all(self.rotation_matrix != other.rotation_matrix):
            return False
        if all(self.vel_vector != other.vel_vector):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def ft_vector(self):
        """Message field 'ft_vector'."""
        return self._ft_vector

    @ft_vector.setter
    def ft_vector(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'ft_vector' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 6, \
                "The 'ft_vector' numpy.ndarray() must have a size of 6"
            self._ft_vector = value
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
                "The 'ft_vector' field must be a set or sequence with length 6 and each value of type 'float'"
        self._ft_vector = numpy.array(value, dtype=numpy.float64)

    @property
    def pos_vector(self):
        """Message field 'pos_vector'."""
        return self._pos_vector

    @pos_vector.setter
    def pos_vector(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'pos_vector' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 3, \
                "The 'pos_vector' numpy.ndarray() must have a size of 3"
            self._pos_vector = value
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
                 len(value) == 3 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'pos_vector' field must be a set or sequence with length 3 and each value of type 'float'"
        self._pos_vector = numpy.array(value, dtype=numpy.float64)

    @property
    def rotation_matrix(self):
        """Message field 'rotation_matrix'."""
        return self._rotation_matrix

    @rotation_matrix.setter
    def rotation_matrix(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'rotation_matrix' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 9, \
                "The 'rotation_matrix' numpy.ndarray() must have a size of 9"
            self._rotation_matrix = value
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
                 len(value) == 9 and
                 all(isinstance(v, float) for v in value) and
                 True), \
                "The 'rotation_matrix' field must be a set or sequence with length 9 and each value of type 'float'"
        self._rotation_matrix = numpy.array(value, dtype=numpy.float64)

    @property
    def vel_vector(self):
        """Message field 'vel_vector'."""
        return self._vel_vector

    @vel_vector.setter
    def vel_vector(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'vel_vector' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 6, \
                "The 'vel_vector' numpy.ndarray() must have a size of 6"
            self._vel_vector = value
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
                "The 'vel_vector' field must be a set or sequence with length 6 and each value of type 'float'"
        self._vel_vector = numpy.array(value, dtype=numpy.float64)
