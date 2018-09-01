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


class TodoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def todo_add_post(self, parameters, **kwargs):  # noqa: E501
        """Adds a problem to todo list.  # noqa: E501

        Takes problemCode and contestCode of the problem to be added. Look at the samples for example  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_add_post(parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param AddTodoParameters parameters: Takes problemCode, contestCode (required)
        :return: list[InlineResponse20015]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.todo_add_post_with_http_info(parameters, **kwargs)  # noqa: E501
        else:
            (data) = self.todo_add_post_with_http_info(parameters, **kwargs)  # noqa: E501
            return data

    def todo_add_post_with_http_info(self, parameters, **kwargs):  # noqa: E501
        """Adds a problem to todo list.  # noqa: E501

        Takes problemCode and contestCode of the problem to be added. Look at the samples for example  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_add_post_with_http_info(parameters, async=True)
        >>> result = thread.get()

        :param async bool
        :param AddTodoParameters parameters: Takes problemCode, contestCode (required)
        :return: list[InlineResponse20015]
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
                    " to method todo_add_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parameters' is set
        if ('parameters' not in params or
                params['parameters'] is None):
            raise ValueError("Missing the required parameter `parameters` when calling `todo_add_post`")  # noqa: E501

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
            '/todo/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20015]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def todo_delete_all_delete(self, **kwargs):  # noqa: E501
        """Deletes all the problems added to the todo list.  # noqa: E501

        Takes no parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_delete_all_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InlineResponse20016]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.todo_delete_all_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.todo_delete_all_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def todo_delete_all_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes all the problems added to the todo list.  # noqa: E501

        Takes no parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_delete_all_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InlineResponse20016]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method todo_delete_all_delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/todo/delete/all', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20016]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def todo_delete_delete(self, problem_code, **kwargs):  # noqa: E501
        """Deletes a problem added to the todo list.  # noqa: E501

        Takes problem code as parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_delete_delete(problem_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str problem_code: Username of the user. (required)
        :return: list[InlineResponse20016]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.todo_delete_delete_with_http_info(problem_code, **kwargs)  # noqa: E501
        else:
            (data) = self.todo_delete_delete_with_http_info(problem_code, **kwargs)  # noqa: E501
            return data

    def todo_delete_delete_with_http_info(self, problem_code, **kwargs):  # noqa: E501
        """Deletes a problem added to the todo list.  # noqa: E501

        Takes problem code as parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_delete_delete_with_http_info(problem_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str problem_code: Username of the user. (required)
        :return: list[InlineResponse20016]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['problem_code']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method todo_delete_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'problem_code' is set
        if ('problem_code' not in params or
                params['problem_code'] is None):
            raise ValueError("Missing the required parameter `problem_code` when calling `todo_delete_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'problem_code' in params:
            query_params.append(('problemCode', params['problem_code']))  # noqa: E501

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
            '/todo/delete/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse20016]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def todo_problems_get(self, **kwargs):  # noqa: E501
        """Gets problems listed in todo.  # noqa: E501

        Takes no paramters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_problems_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Possible fields are- problemCode, contestCode, creationTime, status, tags, problemName, contestUrl, problemUrl, problemRedirect. Multiple fields can be entered using comma.
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.todo_problems_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.todo_problems_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def todo_problems_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets problems listed in todo.  # noqa: E501

        Takes no paramters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.todo_problems_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str fields: Possible fields are- problemCode, contestCode, creationTime, status, tags, problemName, contestUrl, problemUrl, problemRedirect. Multiple fields can be entered using comma.
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method todo_problems_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

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
            '/todo/problems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)