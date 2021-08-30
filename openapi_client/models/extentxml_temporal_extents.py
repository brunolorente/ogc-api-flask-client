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


class ExtentxmlTemporalExtents(object):
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
        'trs': 'str',
        'begin': 'ExtentxmlBegin',
        'end': 'ExtentxmlBegin'
    }

    attribute_map = {
        'trs': 'trs',
        'begin': 'begin',
        'end': 'end'
    }

    def __init__(self, trs='http://www.opengis.net/def/uom/ISO-8601/0/Gregorian', begin=None, end=None):  # noqa: E501
        """ExtentxmlTemporalExtents - a model defined in OpenAPI"""  # noqa: E501

        self._trs = None
        self._begin = None
        self._end = None
        self.discriminator = None

        if trs is not None:
            self.trs = trs
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end

    @property
    def trs(self):
        """Gets the trs of this ExtentxmlTemporalExtents.  # noqa: E501


        :return: The trs of this ExtentxmlTemporalExtents.  # noqa: E501
        :rtype: str
        """
        return self._trs

    @trs.setter
    def trs(self, trs):
        """Sets the trs of this ExtentxmlTemporalExtents.


        :param trs: The trs of this ExtentxmlTemporalExtents.  # noqa: E501
        :type: str
        """

        self._trs = trs

    @property
    def begin(self):
        """Gets the begin of this ExtentxmlTemporalExtents.  # noqa: E501


        :return: The begin of this ExtentxmlTemporalExtents.  # noqa: E501
        :rtype: ExtentxmlBegin
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this ExtentxmlTemporalExtents.


        :param begin: The begin of this ExtentxmlTemporalExtents.  # noqa: E501
        :type: ExtentxmlBegin
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this ExtentxmlTemporalExtents.  # noqa: E501


        :return: The end of this ExtentxmlTemporalExtents.  # noqa: E501
        :rtype: ExtentxmlBegin
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ExtentxmlTemporalExtents.


        :param end: The end of this ExtentxmlTemporalExtents.  # noqa: E501
        :type: ExtentxmlBegin
        """

        self._end = end

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
        if not isinstance(other, ExtentxmlTemporalExtents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other