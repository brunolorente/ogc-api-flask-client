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


class MapInfoStyles(object):
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
        'id': 'str',
        'title': 'str',
        'links': 'list[LinkJson]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'links': 'links'
    }

    def __init__(self, id=None, title=None, links=None):  # noqa: E501
        """MapInfoStyles - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._title = None
        self._links = None
        self.discriminator = None

        self.id = id
        if title is not None:
            self.title = title
        self.links = links

    @property
    def id(self):
        """Gets the id of this MapInfoStyles.  # noqa: E501


        :return: The id of this MapInfoStyles.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MapInfoStyles.


        :param id: The id of this MapInfoStyles.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this MapInfoStyles.  # noqa: E501


        :return: The title of this MapInfoStyles.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MapInfoStyles.


        :param title: The title of this MapInfoStyles.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def links(self):
        """Gets the links of this MapInfoStyles.  # noqa: E501


        :return: The links of this MapInfoStyles.  # noqa: E501
        :rtype: list[LinkJson]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MapInfoStyles.


        :param links: The links of this MapInfoStyles.  # noqa: E501
        :type: list[LinkJson]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

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
        if not isinstance(other, MapInfoStyles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other