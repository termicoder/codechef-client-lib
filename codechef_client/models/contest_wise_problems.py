# coding: utf-8

"""
    CodeChef API

    CodeChef API to support different applications.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ContestWiseProblems(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'contest_code': 'list[str]'
    }

    attribute_map = {
        'contest_code': 'contestCode'
    }

    def __init__(self, contest_code=None):  # noqa: E501
        """ContestWiseProblems - a model defined in Swagger"""  # noqa: E501

        self._contest_code = None
        self.discriminator = None

        if contest_code is not None:
            self.contest_code = contest_code

    @property
    def contest_code(self):
        """Gets the contest_code of this ContestWiseProblems.  # noqa: E501

        Array of problems from the contest depending on criteria.  # noqa: E501

        :return: The contest_code of this ContestWiseProblems.  # noqa: E501
        :rtype: list[str]
        """
        return self._contest_code

    @contest_code.setter
    def contest_code(self, contest_code):
        """Sets the contest_code of this ContestWiseProblems.

        Array of problems from the contest depending on criteria.  # noqa: E501

        :param contest_code: The contest_code of this ContestWiseProblems.  # noqa: E501
        :type: list[str]
        """

        self._contest_code = contest_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ContestWiseProblems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
