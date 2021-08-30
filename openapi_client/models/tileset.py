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


class Tileset(object):
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
        'tile_matrix_set_uri': 'str',
        'tile_matrix_set_definition': 'str',
        'well_known_scale_set': 'str',
        'data_type': 'str',
        'links': 'list[LinkJson]'
    }

    attribute_map = {
        'tile_matrix_set_uri': 'tileMatrixSetURI',
        'tile_matrix_set_definition': 'tileMatrixSetDefinition',
        'well_known_scale_set': 'wellKnownScaleSet',
        'data_type': 'dataType',
        'links': 'links'
    }

    def __init__(self, tile_matrix_set_uri=None, tile_matrix_set_definition=None, well_known_scale_set=None, data_type=None, links=None):  # noqa: E501
        """Tileset - a model defined in OpenAPI"""  # noqa: E501

        self._tile_matrix_set_uri = None
        self._tile_matrix_set_definition = None
        self._well_known_scale_set = None
        self._data_type = None
        self._links = None
        self.discriminator = None

        if tile_matrix_set_uri is not None:
            self.tile_matrix_set_uri = tile_matrix_set_uri
        if tile_matrix_set_definition is not None:
            self.tile_matrix_set_definition = tile_matrix_set_definition
        if well_known_scale_set is not None:
            self.well_known_scale_set = well_known_scale_set
        if data_type is not None:
            self.data_type = data_type
        self.links = links

    @property
    def tile_matrix_set_uri(self):
        """Gets the tile_matrix_set_uri of this Tileset.  # noqa: E501


        :return: The tile_matrix_set_uri of this Tileset.  # noqa: E501
        :rtype: str
        """
        return self._tile_matrix_set_uri

    @tile_matrix_set_uri.setter
    def tile_matrix_set_uri(self, tile_matrix_set_uri):
        """Sets the tile_matrix_set_uri of this Tileset.


        :param tile_matrix_set_uri: The tile_matrix_set_uri of this Tileset.  # noqa: E501
        :type: str
        """

        self._tile_matrix_set_uri = tile_matrix_set_uri

    @property
    def tile_matrix_set_definition(self):
        """Gets the tile_matrix_set_definition of this Tileset.  # noqa: E501


        :return: The tile_matrix_set_definition of this Tileset.  # noqa: E501
        :rtype: str
        """
        return self._tile_matrix_set_definition

    @tile_matrix_set_definition.setter
    def tile_matrix_set_definition(self, tile_matrix_set_definition):
        """Sets the tile_matrix_set_definition of this Tileset.


        :param tile_matrix_set_definition: The tile_matrix_set_definition of this Tileset.  # noqa: E501
        :type: str
        """

        self._tile_matrix_set_definition = tile_matrix_set_definition

    @property
    def well_known_scale_set(self):
        """Gets the well_known_scale_set of this Tileset.  # noqa: E501


        :return: The well_known_scale_set of this Tileset.  # noqa: E501
        :rtype: str
        """
        return self._well_known_scale_set

    @well_known_scale_set.setter
    def well_known_scale_set(self, well_known_scale_set):
        """Sets the well_known_scale_set of this Tileset.


        :param well_known_scale_set: The well_known_scale_set of this Tileset.  # noqa: E501
        :type: str
        """

        self._well_known_scale_set = well_known_scale_set

    @property
    def data_type(self):
        """Gets the data_type of this Tileset.  # noqa: E501


        :return: The data_type of this Tileset.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this Tileset.


        :param data_type: The data_type of this Tileset.  # noqa: E501
        :type: str
        """
        allowed_values = ["map", "vector", "coverage"]  # noqa: E501
        if data_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def links(self):
        """Gets the links of this Tileset.  # noqa: E501


        :return: The links of this Tileset.  # noqa: E501
        :rtype: list[LinkJson]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Tileset.


        :param links: The links of this Tileset.  # noqa: E501
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
        if not isinstance(other, Tileset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other