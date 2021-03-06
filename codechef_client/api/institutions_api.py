# coding: utf-8

"""
    CodeChef API

    CodeChef API to support different applications.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from codechef_client.api_client import ApiClient


class InstitutionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def institution_get(self, search, **kwargs):  # noqa: E501
        """Get the list of institutions on codechef.  # noqa: E501

        Returns a list of instituitions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.institution_get(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Search string for institution, eg. jaypee (required)
        :param int offset: Starting index of the list
        :param int limit: Number of entities to be fetched, max 100
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.institution_get_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.institution_get_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def institution_get_with_http_info(self, search, **kwargs):  # noqa: E501
        """Get the list of institutions on codechef.  # noqa: E501

        Returns a list of instituitions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.institution_get_with_http_info(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param str search: Search string for institution, eg. jaypee (required)
        :param int offset: Starting index of the list
        :param int limit: Number of entities to be fetched, max 100
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'offset', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method institution_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `institution_get`")  # noqa: E501

        if 'limit' in params and params['limit'] > 100:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `institution_get`, must be a value less than or equal to `100`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['codechef_auth']  # noqa: E501

        return self.api_client.call_api(
            '/institution', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
