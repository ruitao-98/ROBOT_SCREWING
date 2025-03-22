# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robot_msgs:msg/FtPub.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FtPub(type):
    """Metaclass of message 'FtPub'."""

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
                'robot_msgs.msg.FtPub')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__ft_pub
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__ft_pub
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__ft_pub
            cls._TYPE_SUPPORT = module.type_support_msg__msg__ft_pub
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__ft_pub

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FtPub(metaclass=Metaclass_FtPub):
    """Message class 'FtPub'."""

    __slots__ = [
        '_fx',
        '_fy',
        '_fz',
        '_tx',
        '_ty',
        '_tz',
    ]

    _fields_and_field_types = {
        'fx': 'float',
        'fy': 'float',
        'fz': 'float',
        'tx': 'float',
        'ty': 'float',
        'tz': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.fx = kwargs.get('fx', float())
        self.fy = kwargs.get('fy', float())
        self.fz = kwargs.get('fz', float())
        self.tx = kwargs.get('tx', float())
        self.ty = kwargs.get('ty', float())
        self.tz = kwargs.get('tz', float())

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
        if self.fx != other.fx:
            return False
        if self.fy != other.fy:
            return False
        if self.fz != other.fz:
            return False
        if self.tx != other.tx:
            return False
        if self.ty != other.ty:
            return False
        if self.tz != other.tz:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def fx(self):
        """Message field 'fx'."""
        return self._fx

    @fx.setter
    def fx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fx' field must be of type 'float'"
        self._fx = value

    @property
    def fy(self):
        """Message field 'fy'."""
        return self._fy

    @fy.setter
    def fy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fy' field must be of type 'float'"
        self._fy = value

    @property
    def fz(self):
        """Message field 'fz'."""
        return self._fz

    @fz.setter
    def fz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'fz' field must be of type 'float'"
        self._fz = value

    @property
    def tx(self):
        """Message field 'tx'."""
        return self._tx

    @tx.setter
    def tx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tx' field must be of type 'float'"
        self._tx = value

    @property
    def ty(self):
        """Message field 'ty'."""
        return self._ty

    @ty.setter
    def ty(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ty' field must be of type 'float'"
        self._ty = value

    @property
    def tz(self):
        """Message field 'tz'."""
        return self._tz

    @tz.setter
    def tz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tz' field must be of type 'float'"
        self._tz = value
