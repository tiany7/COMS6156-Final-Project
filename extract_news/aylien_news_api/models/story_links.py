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


class StoryLinks(object):
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
        'canonical': 'str',
        'permalink': 'str',
        'related_stories': 'str',
        'clusters': 'str'
    }

    attribute_map = {
        'canonical': 'canonical',
        'permalink': 'permalink',
        'related_stories': 'related_stories',
        'clusters': 'clusters'
    }

    def __init__(self, canonical=None, permalink=None, related_stories=None, clusters=None, local_vars_configuration=None):  # noqa: E501
        """StoryLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._canonical = None
        self._permalink = None
        self._related_stories = None
        self._clusters = None
        self.discriminator = None

        if canonical is not None:
            self.canonical = canonical
        if permalink is not None:
            self.permalink = permalink
        if related_stories is not None:
            self.related_stories = related_stories
        if clusters is not None:
            self.clusters = clusters

    @property
    def canonical(self):
        """Gets the canonical of this StoryLinks.  # noqa: E501

        The story canonical URL  # noqa: E501

        :return: The canonical of this StoryLinks.  # noqa: E501
        :rtype: str
        """
        return self._canonical

    @canonical.setter
    def canonical(self, canonical):
        """Sets the canonical of this StoryLinks.

        The story canonical URL  # noqa: E501

        :param canonical: The canonical of this StoryLinks.  # noqa: E501
        :type canonical: str
        """

        self._canonical = canonical

    @property
    def permalink(self):
        """Gets the permalink of this StoryLinks.  # noqa: E501

        The story permalink URL  # noqa: E501

        :return: The permalink of this StoryLinks.  # noqa: E501
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """Sets the permalink of this StoryLinks.

        The story permalink URL  # noqa: E501

        :param permalink: The permalink of this StoryLinks.  # noqa: E501
        :type permalink: str
        """

        self._permalink = permalink

    @property
    def related_stories(self):
        """Gets the related_stories of this StoryLinks.  # noqa: E501

        The related stories URL  # noqa: E501

        :return: The related_stories of this StoryLinks.  # noqa: E501
        :rtype: str
        """
        return self._related_stories

    @related_stories.setter
    def related_stories(self, related_stories):
        """Sets the related_stories of this StoryLinks.

        The related stories URL  # noqa: E501

        :param related_stories: The related_stories of this StoryLinks.  # noqa: E501
        :type related_stories: str
        """

        self._related_stories = related_stories

    @property
    def clusters(self):
        """Gets the clusters of this StoryLinks.  # noqa: E501

        The clusters endpoint URL for this story  # noqa: E501

        :return: The clusters of this StoryLinks.  # noqa: E501
        :rtype: str
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this StoryLinks.

        The clusters endpoint URL for this story  # noqa: E501

        :param clusters: The clusters of this StoryLinks.  # noqa: E501
        :type clusters: str
        """

        self._clusters = clusters

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
        if not isinstance(other, StoryLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoryLinks):
            return True

        return self.to_dict() != other.to_dict()
