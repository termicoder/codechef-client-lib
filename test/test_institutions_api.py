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
from codechef_client.api.institutions_api import InstitutionsApi  # noqa: E501
from codechef_client.rest import ApiException


class TestInstitutionsApi(unittest.TestCase):
    """InstitutionsApi unit test stubs"""

    def setUp(self):
        self.api = codechef_client.api.institutions_api.InstitutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_institution_get(self):
        """Test case for institution_get

        Get the list of institutions on codechef.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
