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


class CollectionsXml(object):
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
        'service': 'str',
        'version': 'str',
        'links': 'list[LinkXml]',
        'collections': 'list[CollectionInfoXml]'
    }

    attribute_map = {
        'service': 'service',
        'version': 'version',
        'links': 'links',
        'collections': 'collections'
    }

    def __init__(self, service=None, version=None, links=None, collections=None):  # noqa: E501
        """CollectionsXml - a model defined in OpenAPI"""  # noqa: E501

        self._service = None
        self._version = None
        self._links = None
        self._collections = None
        self.discriminator = None

        self.service = service
        self.version = version
        self.links = links
        self.collections = collections

    @property
    def service(self):
        """Gets the service of this CollectionsXml.  # noqa: E501


        :return: The service of this CollectionsXml.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this CollectionsXml.


        :param service: The service of this CollectionsXml.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def version(self):
        """Gets the version of this CollectionsXml.  # noqa: E501


        :return: The version of this CollectionsXml.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CollectionsXml.


        :param version: The version of this CollectionsXml.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if version is not None and not re.search(r'(\d\.\d)(\.\d)?', version):  # noqa: E501
            raise ValueError(r"Invalid value for `version`, must be a follow pattern or equal to `/(\d\.\d)(\.\d)?/`")  # noqa: E501

        self._version = version

    @property
    def links(self):
        """Gets the links of this CollectionsXml.  # noqa: E501


        :return: The links of this CollectionsXml.  # noqa: E501
        :rtype: list[LinkXml]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionsXml.


        :param links: The links of this CollectionsXml.  # noqa: E501
        :type: list[LinkXml]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def collections(self):
        """Gets the collections of this CollectionsXml.  # noqa: E501


        :return: The collections of this CollectionsXml.  # noqa: E501
        :rtype: list[CollectionInfoXml]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this CollectionsXml.


        :param collections: The collections of this CollectionsXml.  # noqa: E501
        :type: list[CollectionInfoXml]
        """
        if collections is None:
            raise ValueError("Invalid value for `collections`, must not be `None`")  # noqa: E501

        self._collections = collections

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
        if not isinstance(other, CollectionsXml):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
