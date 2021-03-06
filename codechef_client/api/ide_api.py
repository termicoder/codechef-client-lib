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


class IDEApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ide_run_post(self, parameters, **kwargs):  # noqa: E501
        """Runs a code submitted by user.  # noqa: E501

        Takes input, language and sourceCode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ide_run_post(parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param IdeRunSourceCode parameters: Enter the source code, language, input to be executed. look at samples for example. (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ide_run_post_with_http_info(parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.ide_run_post_with_http_info(parameters, **kwargs)  # noqa: E501
            return data

    def ide_run_post_with_http_info(self, parameters, **kwargs):  # noqa: E501
        """Runs a code submitted by user.  # noqa: E501

        Takes input, language and sourceCode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ide_run_post_with_http_info(parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param IdeRunSourceCode parameters: Enter the source code, language, input to be executed. look at samples for example. (required)
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parameters']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ide_run_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parameters' is set
        if ('parameters' not in params or
                params['parameters'] is None):
            raise ValueError("Missing the required parameter `parameters` when calling `ide_run_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'parameters' in params:
            body_params = params['parameters']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['codechef_auth']  # noqa: E501

        return self.api_client.call_api(
            '/ide/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ide_status_get(self, link, **kwargs):  # noqa: E501
        """Get status of submitted code.  # noqa: E501

        Takes link  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ide_status_get(link, async=True)
        >>> result = thread.get()

        :param async bool
        :param str link: Enter status code recieved after code execution.    eg. VGQUp0 (required)
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ide_status_get_with_http_info(link, **kwargs)  # noqa: E501
        else:
            (data) = self.ide_status_get_with_http_info(link, **kwargs)  # noqa: E501
            return data

    def ide_status_get_with_http_info(self, link, **kwargs):  # noqa: E501
        """Get status of submitted code.  # noqa: E501

        Takes link  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ide_status_get_with_http_info(link, async=True)
        >>> result = thread.get()

        :param async bool
        :param str link: Enter status code recieved after code execution.    eg. VGQUp0 (required)
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['link']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ide_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'link' is set
        if ('link' not in params or
                params['link'] is None):
            raise ValueError("Missing the required parameter `link` when calling `ide_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'link' in params:
            query_params.append(('link', params['link']))  # noqa: E501

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
            '/ide/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20023',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
