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


class TilesInfoTileMatrixSetLinks(object):
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
        'tile_matrix_set': 'str',
        'tile_matrix_set_uri': 'str'
    }

    attribute_map = {
        'tile_matrix_set': 'tileMatrixSet',
        'tile_matrix_set_uri': 'tileMatrixSetURI'
    }

    def __init__(self, tile_matrix_set=None, tile_matrix_set_uri=None):  # noqa: E501
        """TilesInfoTileMatrixSetLinks - a model defined in OpenAPI"""  # noqa: E501

        self._tile_matrix_set = None
        self._tile_matrix_set_uri = None
        self.discriminator = None

        self.tile_matrix_set = tile_matrix_set
        if tile_matrix_set_uri is not None:
            self.tile_matrix_set_uri = tile_matrix_set_uri

    @property
    def tile_matrix_set(self):
        """Gets the tile_matrix_set of this TilesInfoTileMatrixSetLinks.  # noqa: E501


        :return: The tile_matrix_set of this TilesInfoTileMatrixSetLinks.  # noqa: E501
        :rtype: str
        """
        return self._tile_matrix_set

    @tile_matrix_set.setter
    def tile_matrix_set(self, tile_matrix_set):
        """Sets the tile_matrix_set of this TilesInfoTileMatrixSetLinks.


        :param tile_matrix_set: The tile_matrix_set of this TilesInfoTileMatrixSetLinks.  # noqa: E501
        :type: str
        """
        if tile_matrix_set is None:
            raise ValueError("Invalid value for `tile_matrix_set`, must not be `None`")  # noqa: E501

        self._tile_matrix_set = tile_matrix_set

    @property
    def tile_matrix_set_uri(self):
        """Gets the tile_matrix_set_uri of this TilesInfoTileMatrixSetLinks.  # noqa: E501


        :return: The tile_matrix_set_uri of this TilesInfoTileMatrixSetLinks.  # noqa: E501
        :rtype: str
        """
        return self._tile_matrix_set_uri

    @tile_matrix_set_uri.setter
    def tile_matrix_set_uri(self, tile_matrix_set_uri):
        """Sets the tile_matrix_set_uri of this TilesInfoTileMatrixSetLinks.


        :param tile_matrix_set_uri: The tile_matrix_set_uri of this TilesInfoTileMatrixSetLinks.  # noqa: E501
        :type: str
        """

        self._tile_matrix_set_uri = tile_matrix_set_uri

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
        if not isinstance(other, TilesInfoTileMatrixSetLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
