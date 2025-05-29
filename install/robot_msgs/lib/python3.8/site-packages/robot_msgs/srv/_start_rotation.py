# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robot_msgs:srv/StartRotation.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StartRotation_Request(type):
    """Metaclass of message 'StartRotation_Request'."""

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
                'robot_msgs.srv.StartRotation_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_rotation__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_rotation__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_rotation__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_rotation__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_rotation__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StartRotation_Request(metaclass=Metaclass_StartRotation_Request):
    """Message class 'StartRotation_Request'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

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
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

# Member 'pos_para'
# Member 'ori_para'
import numpy  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_StartRotation_Response(type):
    """Metaclass of message 'StartRotation_Response'."""

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
                'robot_msgs.srv.StartRotation_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__start_rotation__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__start_rotation__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__start_rotation__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__start_rotation__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__start_rotation__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class StartRotation_Response(metaclass=Metaclass_StartRotation_Response):
    """Message class 'StartRotation_Response'."""

    __slots__ = [
        '_success',
        '_message',
        '_rotation_speed',
        '_screw_pitch',
        '_pos_para',
        '_ori_para',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
        'rotation_speed': 'double',
        'screw_pitch': 'double',
        'pos_para': 'double[3]',
        'ori_para': 'double[9]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 3),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 9),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())
        self.rotation_speed = kwargs.get('rotation_speed', float())
        self.screw_pitch = kwargs.get('screw_pitch', float())
        if 'pos_para' not in kwargs:
            self.pos_para = numpy.zeros(3, dtype=numpy.float64)
        else:
            self.pos_para = numpy.array(kwargs.get('pos_para'), dtype=numpy.float64)
            assert self.pos_para.shape == (3, )
        if 'ori_para' not in kwargs:
            self.ori_para = numpy.zeros(9, dtype=numpy.float64)
        else:
            self.ori_para = numpy.array(kwargs.get('ori_para'), dtype=numpy.float64)
            assert self.ori_para.shape == (9, )

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
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        if self.rotation_speed != other.rotation_speed:
            return False
        if self.screw_pitch != other.screw_pitch:
            return False
        if all(self.pos_para != other.pos_para):
            return False
        if all(self.ori_para != other.ori_para):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value

    @property
    def rotation_speed(self):
        """Message field 'rotation_speed'."""
        return self._rotation_speed

    @rotation_speed.setter
    def rotation_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'rotation_speed' field must be of type 'float'"
        self._rotation_speed = value

    @property
    def screw_pitch(self):
        """Message field 'screw_pitch'."""
        return self._screw_pitch

    @screw_pitch.setter
    def screw_pitch(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'screw_pitch' field must be of type 'float'"
        self._screw_pitch = value

    @property
    def pos_para(self):
        """Message field 'pos_para'."""
        return self._pos_para

    @pos_para.setter
    def pos_para(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'pos_para' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 3, \
                "The 'pos_para' numpy.ndarray() must have a size of 3"
            self._pos_para = value
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
                "The 'pos_para' field must be a set or sequence with length 3 and each value of type 'float'"
        self._pos_para = numpy.array(value, dtype=numpy.float64)

    @property
    def ori_para(self):
        """Message field 'ori_para'."""
        return self._ori_para

    @ori_para.setter
    def ori_para(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'ori_para' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 9, \
                "The 'ori_para' numpy.ndarray() must have a size of 9"
            self._ori_para = value
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
                "The 'ori_para' field must be a set or sequence with length 9 and each value of type 'float'"
        self._ori_para = numpy.array(value, dtype=numpy.float64)


class Metaclass_StartRotation(type):
    """Metaclass of service 'StartRotation'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robot_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robot_msgs.srv.StartRotation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__start_rotation

            from robot_msgs.srv import _start_rotation
            if _start_rotation.Metaclass_StartRotation_Request._TYPE_SUPPORT is None:
                _start_rotation.Metaclass_StartRotation_Request.__import_type_support__()
            if _start_rotation.Metaclass_StartRotation_Response._TYPE_SUPPORT is None:
                _start_rotation.Metaclass_StartRotation_Response.__import_type_support__()


class StartRotation(metaclass=Metaclass_StartRotation):
    from robot_msgs.srv._start_rotation import StartRotation_Request as Request
    from robot_msgs.srv._start_rotation import StartRotation_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
