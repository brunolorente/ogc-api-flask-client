# coding: utf-8

"""
    Daraa

    This data store is offered by CubeWerx Inc. as a demonstration of its in-progress OGC API implementation.  # noqa: E501

    The version of the OpenAPI document: 9.3.45
    Contact: mgalluch@cubewerx.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class CollectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def collections_collection_id_get(self, collection_id, **kwargs):  # noqa: E501
        """A collection available in this data store.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collections_collection_id_get(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: The identifier of a collection in this data store. (required)
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: CollectionInfoJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.collections_collection_id_get_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collection_id_get_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def collections_collection_id_get_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """A collection available in this data store.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collections_collection_id_get_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: The identifier of a collection in this data store. (required)
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: CollectionInfoJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['collection_id', 'f', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collection_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in local_var_params or
                local_var_params['collection_id'] is None):
            raise ApiValueError("Missing the required parameter `collection_id` when calling `collections_collection_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in local_var_params:
            path_params['collectionId'] = local_var_params['collection_id']  # noqa: E501

        query_params = []
        if 'f' in local_var_params:
            query_params.append(('f', local_var_params['f']))  # noqa: E501
        if 'pretty' in local_var_params:
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/xml', 'text/html', 'application/problem+json', ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cwApiKeyHeader', 'cwApiKeyQuery', 'cwAuth', 'httpBearer', 'oauth2', 'openIdConnect', 'openIdConnect1']  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionInfoJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_get(self, **kwargs):  # noqa: E501
        """The set of collections available in this data store.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collections_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of items to present in the response document.
        :param int offset: The zero-based index within the result set from which the server will begin presenting results in the response document.  If offset is greater or equal to the number of items in the result set, the server will return an empty list.
        :param list[float] bbox: Only elements that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (elevation or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Lower left corner, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Upper right corner, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified by the 'bbox-crs' parameter.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If an element has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.
        :param str bbox_crs: The coordinate reference system of the specified bbox.
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: CollectionsJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.collections_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.collections_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def collections_get_with_http_info(self, **kwargs):  # noqa: E501
        """The set of collections available in this data store.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.collections_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The maximum number of items to present in the response document.
        :param int offset: The zero-based index within the result set from which the server will begin presenting results in the response document.  If offset is greater or equal to the number of items in the result set, the server will return an empty list.
        :param list[float] bbox: Only elements that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (elevation or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Lower left corner, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Upper right corner, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified by the 'bbox-crs' parameter.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If an element has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.
        :param str bbox_crs: The coordinate reference system of the specified bbox.
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: CollectionsJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'offset', 'bbox', 'bbox_crs', 'f', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'limit' in local_var_params and local_var_params['limit'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `collections_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `collections_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if ('bbox' in local_var_params and
                len(local_var_params['bbox']) > 6):
            raise ApiValueError("Invalid value for parameter `bbox` when calling `collections_get`, number of items must be less than or equal to `6`")  # noqa: E501
        if ('bbox' in local_var_params and
                len(local_var_params['bbox']) < 4):
            raise ApiValueError("Invalid value for parameter `bbox` when calling `collections_get`, number of items must be greater than or equal to `4`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'bbox' in local_var_params:
            query_params.append(('bbox', local_var_params['bbox']))  # noqa: E501
            collection_formats['bbox'] = 'csv'  # noqa: E501
        if 'bbox_crs' in local_var_params:
            query_params.append(('bbox-crs', local_var_params['bbox_crs']))  # noqa: E501
        if 'f' in local_var_params:
            query_params.append(('f', local_var_params['f']))  # noqa: E501
        if 'pretty' in local_var_params:
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/xml', 'text/html', 'application/problem+json', ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cwApiKeyHeader', 'cwApiKeyQuery', 'cwAuth', 'httpBearer', 'oauth2', 'openIdConnect', 'openIdConnect1']  # noqa: E501

        return self.api_client.call_api(
            '/collections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionsJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def themes_get(self, **kwargs):  # noqa: E501
        """The set of collections available in this data store, organized into a theme hierarchy (see OGC 18-045, section A.6).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] bbox: Only elements that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (elevation or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Lower left corner, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Upper right corner, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified by the 'bbox-crs' parameter.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If an element has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.
        :param str bbox_crs: The coordinate reference system of the specified bbox.
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param str mode: Experimental.  If \"full\", the complete collection objects are returned.  If \"refsOnly\", only references to the collections are returned.  If \"idsOnly\", only the collection IDs are returned.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: ThemesJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.themes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.themes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def themes_get_with_http_info(self, **kwargs):  # noqa: E501
        """The set of collections available in this data store, organized into a theme hierarchy (see OGC 18-045, section A.6).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.themes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[float] bbox: Only elements that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (elevation or depth):  * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Lower left corner, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Upper right corner, coordinate axis 3 (optional)  The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified by the 'bbox-crs' parameter.  For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge).  If an element has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.
        :param str bbox_crs: The coordinate reference system of the specified bbox.
        :param str f: A token indicating the content type to return.  Overrides the HTTP \"Accept\" header if present.
        :param str mode: Experimental.  If \"full\", the complete collection objects are returned.  If \"refsOnly\", only references to the collections are returned.  If \"idsOnly\", only the collection IDs are returned.
        :param bool pretty: Whether or not the output should be pretty-formatted (with whitespace, etc.).
        :return: ThemesJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['bbox', 'bbox_crs', 'f', 'mode', 'pretty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method themes_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('bbox' in local_var_params and
                len(local_var_params['bbox']) > 6):
            raise ApiValueError("Invalid value for parameter `bbox` when calling `themes_get`, number of items must be less than or equal to `6`")  # noqa: E501
        if ('bbox' in local_var_params and
                len(local_var_params['bbox']) < 4):
            raise ApiValueError("Invalid value for parameter `bbox` when calling `themes_get`, number of items must be greater than or equal to `4`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bbox' in local_var_params:
            query_params.append(('bbox', local_var_params['bbox']))  # noqa: E501
            collection_formats['bbox'] = 'csv'  # noqa: E501
        if 'bbox_crs' in local_var_params:
            query_params.append(('bbox-crs', local_var_params['bbox_crs']))  # noqa: E501
        if 'f' in local_var_params:
            query_params.append(('f', local_var_params['f']))  # noqa: E501
        if 'mode' in local_var_params:
            query_params.append(('mode', local_var_params['mode']))  # noqa: E501
        if 'pretty' in local_var_params:
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html', 'application/problem+json', 'text/xml', ])  # noqa: E501

        # Authentication setting
        auth_settings = ['cwApiKeyHeader', 'cwApiKeyQuery', 'cwAuth', 'httpBearer', 'oauth2', 'openIdConnect', 'openIdConnect1']  # noqa: E501

        return self.api_client.call_api(
            '/themes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ThemesJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
