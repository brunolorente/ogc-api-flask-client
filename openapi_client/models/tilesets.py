# coding: utf-8

"""
    Daraa

    This data store is offered by CubeWerx Inc. as a demonstration of its in-progress OGC API implementation.  # noqa: E501

    The version of the OpenAPI document: 9.3.45
    Contact: mgalluch@cubewerx.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Tilesets(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'tilesets': 'list[TilesetsTilesets]'
    }

    attribute_map = {
        'tilesets': 'tilesets'
    }

    def __init__(self, tilesets=None):  # noqa: E501
        """Tilesets - a model defined in OpenAPI"""  # noqa: E501

        self._tilesets = None
        self.discriminator = None

        self.tilesets = tilesets

    @property
    def tilesets(self):
        """Gets the tilesets of this Tilesets.  # noqa: E501


        :return: The tilesets of this Tilesets.  # noqa: E501
        :rtype: list[TilesetsTilesets]
        """
        return self._tilesets

    @tilesets.setter
    def tilesets(self, tilesets):
        """Sets the tilesets of this Tilesets.


        :param tilesets: The tilesets of this Tilesets.  # noqa: E501
        :type: list[TilesetsTilesets]
        """
        if tilesets is None:
            raise ValueError("Invalid value for `tilesets`, must not be `None`")  # noqa: E501

        self._tilesets = tilesets

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Tilesets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
