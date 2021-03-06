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


class ContestProblemsList(object):
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
        'code': 'str',
        'successful_submissions': 'int',
        'total_submissions': 'float',
        'partial_submissions': 'float',
        'view_start': 'str',
        'submit_start': 'str',
        'visible_start': 'str',
        'end': 'str'
    }

    attribute_map = {
        'code': 'code',
        'successful_submissions': 'successfulSubmissions',
        'total_submissions': 'totalSubmissions',
        'partial_submissions': 'partialSubmissions',
        'view_start': 'viewStart',
        'submit_start': 'submitStart',
        'visible_start': 'visibleStart',
        'end': 'end'
    }

    def __init__(self, code=None, successful_submissions=None, total_submissions=None, partial_submissions=None, view_start=None, submit_start=None, visible_start=None, end=None):  # noqa: E501
        """ContestProblemsList - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._successful_submissions = None
        self._total_submissions = None
        self._partial_submissions = None
        self._view_start = None
        self._submit_start = None
        self._visible_start = None
        self._end = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if successful_submissions is not None:
            self.successful_submissions = successful_submissions
        if total_submissions is not None:
            self.total_submissions = total_submissions
        if partial_submissions is not None:
            self.partial_submissions = partial_submissions
        if view_start is not None:
            self.view_start = view_start
        if submit_start is not None:
            self.submit_start = submit_start
        if visible_start is not None:
            self.visible_start = visible_start
        if end is not None:
            self.end = end

    @property
    def code(self):
        """Gets the code of this ContestProblemsList.  # noqa: E501

        Problem code  # noqa: E501

        :return: The code of this ContestProblemsList.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ContestProblemsList.

        Problem code  # noqa: E501

        :param code: The code of this ContestProblemsList.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def successful_submissions(self):
        """Gets the successful_submissions of this ContestProblemsList.  # noqa: E501

        Successful submissions by unique users i.e. only the best submission of all submissions made by the user will be taken into account.  # noqa: E501

        :return: The successful_submissions of this ContestProblemsList.  # noqa: E501
        :rtype: int
        """
        return self._successful_submissions

    @successful_submissions.setter
    def successful_submissions(self, successful_submissions):
        """Sets the successful_submissions of this ContestProblemsList.

        Successful submissions by unique users i.e. only the best submission of all submissions made by the user will be taken into account.  # noqa: E501

        :param successful_submissions: The successful_submissions of this ContestProblemsList.  # noqa: E501
        :type: int
        """

        self._successful_submissions = successful_submissions

    @property
    def total_submissions(self):
        """Gets the total_submissions of this ContestProblemsList.  # noqa: E501

        Accuracy of the submissions  # noqa: E501

        :return: The total_submissions of this ContestProblemsList.  # noqa: E501
        :rtype: float
        """
        return self._total_submissions

    @total_submissions.setter
    def total_submissions(self, total_submissions):
        """Sets the total_submissions of this ContestProblemsList.

        Accuracy of the submissions  # noqa: E501

        :param total_submissions: The total_submissions of this ContestProblemsList.  # noqa: E501
        :type: float
        """

        self._total_submissions = total_submissions

    @property
    def partial_submissions(self):
        """Gets the partial_submissions of this ContestProblemsList.  # noqa: E501

        Number  of partial submissions  # noqa: E501

        :return: The partial_submissions of this ContestProblemsList.  # noqa: E501
        :rtype: float
        """
        return self._partial_submissions

    @partial_submissions.setter
    def partial_submissions(self, partial_submissions):
        """Sets the partial_submissions of this ContestProblemsList.

        Number  of partial submissions  # noqa: E501

        :param partial_submissions: The partial_submissions of this ContestProblemsList.  # noqa: E501
        :type: float
        """

        self._partial_submissions = partial_submissions

    @property
    def view_start(self):
        """Gets the view_start of this ContestProblemsList.  # noqa: E501

        Start time of the contest  # noqa: E501

        :return: The view_start of this ContestProblemsList.  # noqa: E501
        :rtype: str
        """
        return self._view_start

    @view_start.setter
    def view_start(self, view_start):
        """Sets the view_start of this ContestProblemsList.

        Start time of the contest  # noqa: E501

        :param view_start: The view_start of this ContestProblemsList.  # noqa: E501
        :type: str
        """

        self._view_start = view_start

    @property
    def submit_start(self):
        """Gets the submit_start of this ContestProblemsList.  # noqa: E501

        Submit start time of the contest  # noqa: E501

        :return: The submit_start of this ContestProblemsList.  # noqa: E501
        :rtype: str
        """
        return self._submit_start

    @submit_start.setter
    def submit_start(self, submit_start):
        """Sets the submit_start of this ContestProblemsList.

        Submit start time of the contest  # noqa: E501

        :param submit_start: The submit_start of this ContestProblemsList.  # noqa: E501
        :type: str
        """

        self._submit_start = submit_start

    @property
    def visible_start(self):
        """Gets the visible_start of this ContestProblemsList.  # noqa: E501

        Visible time of the contest  # noqa: E501

        :return: The visible_start of this ContestProblemsList.  # noqa: E501
        :rtype: str
        """
        return self._visible_start

    @visible_start.setter
    def visible_start(self, visible_start):
        """Sets the visible_start of this ContestProblemsList.

        Visible time of the contest  # noqa: E501

        :param visible_start: The visible_start of this ContestProblemsList.  # noqa: E501
        :type: str
        """

        self._visible_start = visible_start

    @property
    def end(self):
        """Gets the end of this ContestProblemsList.  # noqa: E501

        End time of the contest  # noqa: E501

        :return: The end of this ContestProblemsList.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ContestProblemsList.

        End time of the contest  # noqa: E501

        :param end: The end of this ContestProblemsList.  # noqa: E501
        :type: str
        """

        self._end = end

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
        if not isinstance(other, ContestProblemsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
