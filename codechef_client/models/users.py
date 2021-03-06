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

from codechef_client.models.all_ranking import AllRanking  # noqa: F401,E501
from codechef_client.models.city import City  # noqa: F401,E501
from codechef_client.models.country import Country  # noqa: F401,E501
from codechef_client.models.rating import Rating  # noqa: F401,E501
from codechef_client.models.state import State  # noqa: F401,E501


class Users(object):
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
        'username': 'str',
        'fullname': 'str',
        'country': 'Country',
        'state': 'State',
        'city': 'City',
        'occupation': 'str',
        'organization': 'str',
        'ratings': 'Rating',
        'rankings': 'AllRanking'
    }

    attribute_map = {
        'username': 'username',
        'fullname': 'fullname',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'occupation': 'occupation',
        'organization': 'organization',
        'ratings': 'ratings',
        'rankings': 'rankings'
    }

    def __init__(self, username=None, fullname=None, country=None, state=None, city=None, occupation=None, organization=None, ratings=None, rankings=None):  # noqa: E501
        """Users - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._fullname = None
        self._country = None
        self._state = None
        self._city = None
        self._occupation = None
        self._organization = None
        self._ratings = None
        self._rankings = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if fullname is not None:
            self.fullname = fullname
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if city is not None:
            self.city = city
        if occupation is not None:
            self.occupation = occupation
        if organization is not None:
            self.organization = organization
        if ratings is not None:
            self.ratings = ratings
        if rankings is not None:
            self.rankings = rankings

    @property
    def username(self):
        """Gets the username of this Users.  # noqa: E501

        Unique username of the user.  # noqa: E501

        :return: The username of this Users.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Users.

        Unique username of the user.  # noqa: E501

        :param username: The username of this Users.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def fullname(self):
        """Gets the fullname of this Users.  # noqa: E501

        Fullname of the user.  # noqa: E501

        :return: The fullname of this Users.  # noqa: E501
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this Users.

        Fullname of the user.  # noqa: E501

        :param fullname: The fullname of this Users.  # noqa: E501
        :type: str
        """

        self._fullname = fullname

    @property
    def country(self):
        """Gets the country of this Users.  # noqa: E501


        :return: The country of this Users.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Users.


        :param country: The country of this Users.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this Users.  # noqa: E501


        :return: The state of this Users.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Users.


        :param state: The state of this Users.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def city(self):
        """Gets the city of this Users.  # noqa: E501


        :return: The city of this Users.  # noqa: E501
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Users.


        :param city: The city of this Users.  # noqa: E501
        :type: City
        """

        self._city = city

    @property
    def occupation(self):
        """Gets the occupation of this Users.  # noqa: E501

        The User is a student or a professional.  # noqa: E501

        :return: The occupation of this Users.  # noqa: E501
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """Sets the occupation of this Users.

        The User is a student or a professional.  # noqa: E501

        :param occupation: The occupation of this Users.  # noqa: E501
        :type: str
        """

        self._occupation = occupation

    @property
    def organization(self):
        """Gets the organization of this Users.  # noqa: E501

        Institute or organization of the user.  # noqa: E501

        :return: The organization of this Users.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Users.

        Institute or organization of the user.  # noqa: E501

        :param organization: The organization of this Users.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def ratings(self):
        """Gets the ratings of this Users.  # noqa: E501


        :return: The ratings of this Users.  # noqa: E501
        :rtype: Rating
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this Users.


        :param ratings: The ratings of this Users.  # noqa: E501
        :type: Rating
        """

        self._ratings = ratings

    @property
    def rankings(self):
        """Gets the rankings of this Users.  # noqa: E501


        :return: The rankings of this Users.  # noqa: E501
        :rtype: AllRanking
        """
        return self._rankings

    @rankings.setter
    def rankings(self, rankings):
        """Sets the rankings of this Users.


        :param rankings: The rankings of this Users.  # noqa: E501
        :type: AllRanking
        """

        self._rankings = rankings

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
        if not isinstance(other, Users):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
