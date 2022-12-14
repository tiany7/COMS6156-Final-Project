# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.3
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Sentiments(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'body': 'Sentiment',
        'title': 'Sentiment'
    }

    attribute_map = {
        'body': 'body',
        'title': 'title'
    }

    def __init__(self, body=None, title=None, local_vars_configuration=None):  # noqa: E501
        """Sentiments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self._title = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if title is not None:
            self.title = title

    @property
    def body(self):
        """Gets the body of this Sentiments.  # noqa: E501


        :return: The body of this Sentiments.  # noqa: E501
        :rtype: Sentiment
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Sentiments.


        :param body: The body of this Sentiments.  # noqa: E501
        :type body: Sentiment
        """

        self._body = body

    @property
    def title(self):
        """Gets the title of this Sentiments.  # noqa: E501


        :return: The title of this Sentiments.  # noqa: E501
        :rtype: Sentiment
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Sentiments.


        :param title: The title of this Sentiments.  # noqa: E501
        :type title: Sentiment
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Sentiments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sentiments):
            return True

        return self.to_dict() != other.to_dict()
