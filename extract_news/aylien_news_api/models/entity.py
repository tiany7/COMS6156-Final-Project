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


class Entity(object):
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
        'id': 'str',
        'links': 'EntityLinks',
        'stock_tickers': 'list[str]',
        'types': 'list[str]',
        'overall_sentiment': 'EntitySentiment',
        'overall_prominence': 'float',
        'overall_frequency': 'int',
        'body': 'EntityInText',
        'title': 'EntityInText',
        'external_ids': 'ExternalIds'
    }

    attribute_map = {
        'id': 'id',
        'links': 'links',
        'stock_tickers': 'stock_tickers',
        'types': 'types',
        'overall_sentiment': 'overall_sentiment',
        'overall_prominence': 'overall_prominence',
        'overall_frequency': 'overall_frequency',
        'body': 'body',
        'title': 'title',
        'external_ids': 'external_ids'
    }

    def __init__(self, id=None, links=None, stock_tickers=None, types=None, overall_sentiment=None, overall_prominence=None, overall_frequency=None, body=None, title=None, external_ids=None, local_vars_configuration=None):  # noqa: E501
        """Entity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._links = None
        self._stock_tickers = None
        self._types = None
        self._overall_sentiment = None
        self._overall_prominence = None
        self._overall_frequency = None
        self._body = None
        self._title = None
        self._external_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if stock_tickers is not None:
            self.stock_tickers = stock_tickers
        if types is not None:
            self.types = types
        if overall_sentiment is not None:
            self.overall_sentiment = overall_sentiment
        if overall_prominence is not None:
            self.overall_prominence = overall_prominence
        if overall_frequency is not None:
            self.overall_frequency = overall_frequency
        if body is not None:
            self.body = body
        if title is not None:
            self.title = title
        if external_ids is not None:
            self.external_ids = external_ids

    @property
    def id(self):
        """Gets the id of this Entity.  # noqa: E501

        The unique ID of the entity  # noqa: E501

        :return: The id of this Entity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Entity.

        The unique ID of the entity  # noqa: E501

        :param id: The id of this Entity.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this Entity.  # noqa: E501


        :return: The links of this Entity.  # noqa: E501
        :rtype: EntityLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Entity.


        :param links: The links of this Entity.  # noqa: E501
        :type links: EntityLinks
        """

        self._links = links

    @property
    def stock_tickers(self):
        """Gets the stock_tickers of this Entity.  # noqa: E501

        The stock tickers of the entity (might be empty)  # noqa: E501

        :return: The stock_tickers of this Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._stock_tickers

    @stock_tickers.setter
    def stock_tickers(self, stock_tickers):
        """Sets the stock_tickers of this Entity.

        The stock tickers of the entity (might be empty)  # noqa: E501

        :param stock_tickers: The stock_tickers of this Entity.  # noqa: E501
        :type stock_tickers: list[str]
        """

        self._stock_tickers = stock_tickers

    @property
    def types(self):
        """Gets the types of this Entity.  # noqa: E501

        An array of the entity types  # noqa: E501

        :return: The types of this Entity.  # noqa: E501
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this Entity.

        An array of the entity types  # noqa: E501

        :param types: The types of this Entity.  # noqa: E501
        :type types: list[str]
        """

        self._types = types

    @property
    def overall_sentiment(self):
        """Gets the overall_sentiment of this Entity.  # noqa: E501


        :return: The overall_sentiment of this Entity.  # noqa: E501
        :rtype: EntitySentiment
        """
        return self._overall_sentiment

    @overall_sentiment.setter
    def overall_sentiment(self, overall_sentiment):
        """Sets the overall_sentiment of this Entity.


        :param overall_sentiment: The overall_sentiment of this Entity.  # noqa: E501
        :type overall_sentiment: EntitySentiment
        """

        self._overall_sentiment = overall_sentiment

    @property
    def overall_prominence(self):
        """Gets the overall_prominence of this Entity.  # noqa: E501

        Describes how relevant an entity is to the article  # noqa: E501

        :return: The overall_prominence of this Entity.  # noqa: E501
        :rtype: float
        """
        return self._overall_prominence

    @overall_prominence.setter
    def overall_prominence(self, overall_prominence):
        """Sets the overall_prominence of this Entity.

        Describes how relevant an entity is to the article  # noqa: E501

        :param overall_prominence: The overall_prominence of this Entity.  # noqa: E501
        :type overall_prominence: float
        """
        if (self.local_vars_configuration.client_side_validation and
                overall_prominence is not None and overall_prominence > 1):  # noqa: E501
            raise ValueError("Invalid value for `overall_prominence`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                overall_prominence is not None and overall_prominence < 0):  # noqa: E501
            raise ValueError("Invalid value for `overall_prominence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._overall_prominence = overall_prominence

    @property
    def overall_frequency(self):
        """Gets the overall_frequency of this Entity.  # noqa: E501

        Amount of entity surface form mentions in the article  # noqa: E501

        :return: The overall_frequency of this Entity.  # noqa: E501
        :rtype: int
        """
        return self._overall_frequency

    @overall_frequency.setter
    def overall_frequency(self, overall_frequency):
        """Sets the overall_frequency of this Entity.

        Amount of entity surface form mentions in the article  # noqa: E501

        :param overall_frequency: The overall_frequency of this Entity.  # noqa: E501
        :type overall_frequency: int
        """
        if (self.local_vars_configuration.client_side_validation and
                overall_frequency is not None and overall_frequency < 0):  # noqa: E501
            raise ValueError("Invalid value for `overall_frequency`, must be a value greater than or equal to `0`")  # noqa: E501

        self._overall_frequency = overall_frequency

    @property
    def body(self):
        """Gets the body of this Entity.  # noqa: E501


        :return: The body of this Entity.  # noqa: E501
        :rtype: EntityInText
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Entity.


        :param body: The body of this Entity.  # noqa: E501
        :type body: EntityInText
        """

        self._body = body

    @property
    def title(self):
        """Gets the title of this Entity.  # noqa: E501


        :return: The title of this Entity.  # noqa: E501
        :rtype: EntityInText
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Entity.


        :param title: The title of this Entity.  # noqa: E501
        :type title: EntityInText
        """

        self._title = title

    @property
    def external_ids(self):
        """Gets the external_ids of this Entity.  # noqa: E501


        :return: The external_ids of this Entity.  # noqa: E501
        :rtype: ExternalIds
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Entity.


        :param external_ids: The external_ids of this Entity.  # noqa: E501
        :type external_ids: ExternalIds
        """

        self._external_ids = external_ids

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
        if not isinstance(other, Entity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Entity):
            return True

        return self.to_dict() != other.to_dict()
