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
from codechef_client.api.submission_api import SubmissionApi  # noqa: E501
from codechef_client.rest import ApiException


class TestSubmissionApi(unittest.TestCase):
    """SubmissionApi unit test stubs"""

    def setUp(self):
        self.api = codechef_client.api.submission_api.SubmissionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_submissions_get(self):
        """Test case for submissions_get

        Get submissions for particular user, problemCode, result and year.  # noqa: E501
        """
        pass

    def test_submissions_submission_id_get(self):
        """Test case for submissions_submission_id_get

        Get details of a submission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
