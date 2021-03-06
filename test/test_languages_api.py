# coding: utf-8

"""
    CodeChef API

    CodeChef API to support different applications.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import codechef_client
from codechef_client.api.languages_api import LanguagesApi  # noqa: E501
from codechef_client.rest import ApiException


class TestLanguagesApi(unittest.TestCase):
    """LanguagesApi unit test stubs"""

    def setUp(self):
        self.api = codechef_client.api.languages_api.LanguagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_language_get(self):
        """Test case for language_get

        Get the list of languages on codechef.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
