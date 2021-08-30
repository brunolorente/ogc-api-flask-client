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


class LandingPageJson(object):
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
        'title': 'str',
        'description': 'str',
        'attribution': 'str',
        'links': 'list[LinkJson]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'attribution': 'attribution',
        'links': 'links'
    }

    def __init__(self, title=None, description=None, attribution=None, links=None):  # noqa: E501
        """LandingPageJson - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._description = None
        self._attribution = None
        self._links = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        if attribution is not None:
            self.attribution = attribution
        self.links = links

    @property
    def title(self):
        """Gets the title of this LandingPageJson.  # noqa: E501

        The title of the API  # noqa: E501

        :return: The title of this LandingPageJson.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LandingPageJson.

        The title of the API  # noqa: E501

        :param title: The title of this LandingPageJson.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this LandingPageJson.  # noqa: E501

        A textual description of the API  # noqa: E501

        :return: The description of this LandingPageJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LandingPageJson.

        A textual description of the API  # noqa: E501

        :param description: The description of this LandingPageJson.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def attribution(self):
        """Gets the attribution of this LandingPageJson.  # noqa: E501

        An attribution for the API.  It should be short and intended for presentation to a user, for example, in a corner of a map.  Parts of the text can be links to other resources if additional information is needed.  The string can include HTML markup.  # noqa: E501

        :return: The attribution of this LandingPageJson.  # noqa: E501
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this LandingPageJson.

        An attribution for the API.  It should be short and intended for presentation to a user, for example, in a corner of a map.  Parts of the text can be links to other resources if additional information is needed.  The string can include HTML markup.  # noqa: E501

        :param attribution: The attribution of this LandingPageJson.  # noqa: E501
        :type: str
        """

        self._attribution = attribution

    @property
    def links(self):
        """Gets the links of this LandingPageJson.  # noqa: E501

        Links to the resources exposed through this API.  # noqa: E501

        :return: The links of this LandingPageJson.  # noqa: E501
        :rtype: list[LinkJson]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LandingPageJson.

        Links to the resources exposed through this API.  # noqa: E501

        :param links: The links of this LandingPageJson.  # noqa: E501
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
        if not isinstance(other, LandingPageJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
