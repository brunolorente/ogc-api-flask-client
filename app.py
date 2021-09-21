import openapi_client
from openapi_client.rest import ApiException

import json
import time
import requests
from pprint import pprint

from flask import Flask, jsonify, render_template, request, url_for
app = Flask(__name__)
configuration = openapi_client.Configuration()

TILESERVER_URL = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'

# Daraa useful links
useful_links = [
    ('https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa?f=json','Landing page'),
    ('https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa/api?f=json','Api definition'),
    ('https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa/conformance?f=json','Conformance classes'),
    ('https://test.cubewerx.com/cubewerx/cubeserv/demo/ogcapi/Daraa/collections','Collections'),
]

@app.route('/')
def index():
    if not request.root_url:
        # this assumes that the 'index' view function handles the path '/'
        request.root_url = url_for('index', _external=True)
    return render_template('index.html', links=useful_links)

@app.route('/collections/<collectionId>/items/')
def get_features(collectionId):
    # create an instance of the API class
    api_instance = openapi_client.VectorFeaturesAndCatalogueRecordsApi(openapi_client.ApiClient(configuration))
    collection_id = collectionId # str | Name of a feature collection offered by the service
    f = 'json' # str | A MIME type indicating the representation of the resources to be presented (e.g. application/gml+xml; version=3.2 for GML 3.2). (optional)
    if (request.args.get('l')):
        limit = int(request.args.get('l')) # int | The optional limit parameter limits the number of items that are presented in the response document.  Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. (optional) (default to 10)
    else:
        limit = 20 # int | The optional limit parameter limits the number of items that are presented in the response document.  Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. (optional) (default to 10)
    # datetime = '2013-10-20T19:20:30+01:00' # datetime | Temporal constraint to be applied to a query; may be a time instance or a temporal period as per ISO8601. (optional)
    # t_relation = 't_relation_example' # str | Temporal operator to use for temporal contstraint (optional)
    # result_type = 'results' # str | The possible values for this parameter are \"results\" and \"hits\". If the value of the resultType parameter is set to \"results\" the server shall generate a complete response document containing resources that satisfy the operation. The root element of the response container shall include a count of the number of resources actually presented in the response document. The root element of the response container shall also include a count of the total number of resources that the operations actually found which will always be equal to or greater than the number of resource presented in the response document. If the value of the resultType attribute is set to \"hits\" the server shall generate an empty response document containing no resource instances and the root element of the response container shall contain the count of the total number of resources that the operation found. The value for the number of resources presented in the response document shall be set to zero. (optional) (default to 'results')
    # property_name = 'property_name_example' # str | A list of feature properties to include in the response.  For some output formats, such as XML that can be validate against a formal schema, this list represents the optional properties to include in the response. (optional)
    # coord_precision = 56 # int | Number of digits after the decimal point to use when presenting result in a text-base output format such as XML or JSON (optional)
    # css = 'css_example' # str | A reference to a CSS to be applied to HTML-based output formats; ignored otherwise (optional)
    # xslt = 'xslt_example' # str | A reference to a XSLT to be applied to XML-based output formats; ignored otherwise (optional)
    # kml_style_url = 'kml_style_url_example' # str | A reference to a KML style shere to be applied to KML-based output formats; ignored otherwise (optional)
    # max_bytes = 56 # int | The maximum number of bytes to be presented in one page of a query response. (optional)
    # resolution = 3.4 # float | Specifies the resolution of a display port in the event that the WFS output is intended for display; the server attempts to simplify each output geometry by removing unnecessary verticies and this triming the size of the response. (optional)
    # response_handler = 'response_handler_example' # str | Tiggers asynchronous processing of the request; notification is sent to the endpoint specified as the value of the parameter. (optional)
    # crs = 'http://www.opengis.net/def/crs/epsg/0/4326' # str | Asserts the CRS to use for encoding features in the response document. (optional)
    # filter = 'filter_example' # str | A query filter specified is some predicate encoding language supported by the server (optional)
    # filter_language = 'filter_language_example' # str | An identifier indicating the predicate language used to express the value of the \"filter\" parameter (optional)
    # q = 'q_example' # str | A space seperated list of search terms to be applied to text fields in a feature. (optional)
    # geometry = 'geometry_example' # str | The geometry of an area of interest specified using WKT. (optional)
    # geometry_crs = 'geometry_crs_example' # str | The CRS used to encode the coordinates of the \"geometry\" parameter. (optional)
    # relation = 'relation_example' # str | The spatial operator to apply when testing a feature's geometry against the area of interest encoded using the \"geometry\" parameter. (optional)
    # lat = 3.4 # float | The latitude of the center point of a proximity search. (optional)
    # lon = 3.4 # float | The longitude of the center point of a proximity search. (optional)
    # radius = 3.4 # float | The search radius in meters of a proximity search. (optional)
    pretty = True # bool | Whether or not the output should be pretty-formatted (with whitespace, etc.). (optional) (default to False)

    try:
        queriable = request.args.get('queriable_name')
        queriable_value = request.args.get('queriable_value')

        # This operation retreives features from the specified collection
        if (queriable != '' and queriable != None and queriable == 'bbox' and queriable_value != '' and queriable_value != 'None'): # list[float] | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (elevation or depth): * Lower left corner, coordinate axis 1 * Lower left corner, coordinate axis 2 * Lower left corner, coordinate axis 3 (optional) * Upper right corner, coordinate axis 1 * Upper right corner, coordinate axis 2 * Upper right corner, coordinate axis 3 (optional) The coordinate reference system of the values is WGS84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`. For WGS84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge). If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. (optional)
            api_response = api_instance.get_features(collection_id, f=f, limit=limit, pretty=pretty, bbox=queriable_value.split(','))
        else:
            api_response = api_instance.get_features(collection_id, f=f, limit=limit, pretty=pretty)

        # Parsing received string to JSON
        json_api_response = json.loads(api_response.replace("'",'"'))
        # Saving the received features
        json_fearures_list = json_api_response["features"]
        # Return features
        return jsonify(json_fearures_list)
    except ApiException as e:
        return f'Exception when calling VectorFeaturesAndCatalogueRecordsApi->get_features: {e}\n'

@app.route('/collections/<collectionId>/items/<featureId>')
def get_feature(collectionId, featureId):
    # create an instance of the API class
    api_instance = openapi_client.VectorFeaturesAndCatalogueRecordsApi(openapi_client.ApiClient(configuration))
    collection_id = collectionId # str | Name of a feature collection offered by the service
    feature_id = featureId # str | Locate identifier for a specific feature
    f = 'json' # str | A MIME type indicating the representation of the resources to be presented (e.g. application/gml+xml; version=3.2 for GML 3.2). (optional)
    # result_type = 'results' # str | The possible values for this parameter are \"results\" and \"hits\". If the value of the resultType parameter is set to \"results\" the server shall generate a complete response document containing resources that satisfy the operation. The root element of the response container shall include a count of the number of resources actually presented in the response document. The root element of the response container shall also include a count of the total number of resources that the operations actually found which will always be equal to or greater than the number of resource presented in the response document. If the value of the resultType attribute is set to \"hits\" the server shall generate an empty response document containing no resource instances and the root element of the response container shall contain the count of the total number of resources that the operation found. The value for the number of resources presented in the response document shall be set to zero. (optional) (default to 'results')
    # property_name = 'property_name_example' # str | A list of feature properties to include in the response.  For some output formats, such as XML that can be validate against a formal schema, this list represents the optional properties to include in the response. (optional)
    # coord_precision = 56 # int | Number of digits after the decimal point to use when presenting result in a text-base output format such as XML or JSON (optional)
    # css = 'css_example' # str | A reference to a CSS to be applied to HTML-based output formats; ignored otherwise (optional)
    # xslt = 'xslt_example' # str | A reference to a XSLT to be applied to XML-based output formats; ignored otherwise (optional)
    # kml_style_url = 'kml_style_url_example' # str | A reference to a KML style shere to be applied to KML-based output formats; ignored otherwise (optional)
    # resolution = 3.4 # float | Specifies the resolution of a display port in the event that the WFS output is intended for display; the server attempts to simplify each output geometry by removing unnecessary verticies and this triming the size of the response. (optional)
    # response_handler = 'response_handler_example' # str | Tiggers asynchronous processing of the request; notification is sent to the endpoint specified as the value of the parameter. (optional)
    # crs = 'http://www.opengis.net/def/crs/epsg/0/4326' # str | Asserts the CRS to use for encoding features in the response document. (optional)
    pretty = False # bool | Whether or not the output should be pretty-formatted (with whitespace, etc.). (optional) (default to False)

    try:
        # This operation retreives the specified feature from the specified collection
        api_response = api_instance.get_feature(collection_id, feature_id, f=f, pretty=pretty)
        # Parsing received string to JSON
        json_api_response = json.loads(api_response.replace("'",'"'))
        # Saving the received features
        json_fearures_list = json_api_response["features"]
        # Return features
        return jsonify(json_fearures_list)
    except ApiException as e:
        return f'Exception when calling VectorFeaturesAndCatalogueRecordsApi->get_feature: {e}\n'



