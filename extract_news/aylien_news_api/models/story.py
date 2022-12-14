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


class Story(object):
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
        'author': 'Author',
        'body': 'str',
        'categories': 'list[Category]',
        'characters_count': 'int',
        'clusters': 'list[int]',
        'entities': 'list[Entity]',
        'hashtags': 'list[str]',
        'id': 'int',
        'keywords': 'list[str]',
        'language': 'str',
        'links': 'StoryLinks',
        'media': 'list[Media]',
        'paragraphs_count': 'int',
        'published_datetime': 'datetime',
        'published_at': 'datetime',
        'sentences_count': 'int',
        'sentiment': 'Sentiments',
        'social_shares_count': 'ShareCounts',
        'source': 'Source',
        'summary': 'Summary',
        'title': 'str',
        'translations': 'StoryTranslations',
        'words_count': 'int',
        'license_type': 'int',
        'industries': 'list[Category]'
    }

    attribute_map = {
        'author': 'author',
        'body': 'body',
        'categories': 'categories',
        'characters_count': 'characters_count',
        'clusters': 'clusters',
        'entities': 'entities',
        'hashtags': 'hashtags',
        'id': 'id',
        'keywords': 'keywords',
        'language': 'language',
        'links': 'links',
        'media': 'media',
        'paragraphs_count': 'paragraphs_count',
        'published_datetime': 'published_datetime',
        'published_at': 'published_at',
        'sentences_count': 'sentences_count',
        'sentiment': 'sentiment',
        'social_shares_count': 'social_shares_count',
        'source': 'source',
        'summary': 'summary',
        'title': 'title',
        'translations': 'translations',
        'words_count': 'words_count',
        'license_type': 'license_type',
        'industries': 'industries'
    }

    def __init__(self, author=None, body=None, categories=None, characters_count=None, clusters=None, entities=None, hashtags=None, id=None, keywords=None, language=None, links=None, media=None, paragraphs_count=None, published_datetime=None, published_at=None, sentences_count=None, sentiment=None, social_shares_count=None, source=None, summary=None, title=None, translations=None, words_count=None, license_type=None, industries=None, local_vars_configuration=None):  # noqa: E501
        """Story - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._author = None
        self._body = None
        self._categories = None
        self._characters_count = None
        self._clusters = None
        self._entities = None
        self._hashtags = None
        self._id = None
        self._keywords = None
        self._language = None
        self._links = None
        self._media = None
        self._paragraphs_count = None
        self._published_datetime = None
        self._published_at = None
        self._sentences_count = None
        self._sentiment = None
        self._social_shares_count = None
        self._source = None
        self._summary = None
        self._title = None
        self._translations = None
        self._words_count = None
        self._license_type = None
        self._industries = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if body is not None:
            self.body = body
        if categories is not None:
            self.categories = categories
        if characters_count is not None:
            self.characters_count = characters_count
        if clusters is not None:
            self.clusters = clusters
        if entities is not None:
            self.entities = entities
        if hashtags is not None:
            self.hashtags = hashtags
        if id is not None:
            self.id = id
        if keywords is not None:
            self.keywords = keywords
        if language is not None:
            self.language = language
        if links is not None:
            self.links = links
        if media is not None:
            self.media = media
        if paragraphs_count is not None:
            self.paragraphs_count = paragraphs_count
        if published_datetime is not None:
            self.published_datetime = published_datetime
        if published_at is not None:
            self.published_at = published_at
        if sentences_count is not None:
            self.sentences_count = sentences_count
        if sentiment is not None:
            self.sentiment = sentiment
        if social_shares_count is not None:
            self.social_shares_count = social_shares_count
        if source is not None:
            self.source = source
        if summary is not None:
            self.summary = summary
        if title is not None:
            self.title = title
        if translations is not None:
            self.translations = translations
        if words_count is not None:
            self.words_count = words_count
        if license_type is not None:
            self.license_type = license_type
        if industries is not None:
            self.industries = industries

    @property
    def author(self):
        """Gets the author of this Story.  # noqa: E501


        :return: The author of this Story.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Story.


        :param author: The author of this Story.  # noqa: E501
        :type author: Author
        """

        self._author = author

    @property
    def body(self):
        """Gets the body of this Story.  # noqa: E501

        Body of the story  # noqa: E501

        :return: The body of this Story.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Story.

        Body of the story  # noqa: E501

        :param body: The body of this Story.  # noqa: E501
        :type body: str
        """

        self._body = body

    @property
    def categories(self):
        """Gets the categories of this Story.  # noqa: E501

        Suggested categories for the story  # noqa: E501

        :return: The categories of this Story.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Story.

        Suggested categories for the story  # noqa: E501

        :param categories: The categories of this Story.  # noqa: E501
        :type categories: list[Category]
        """

        self._categories = categories

    @property
    def characters_count(self):
        """Gets the characters_count of this Story.  # noqa: E501

        Character count of the story body  # noqa: E501

        :return: The characters_count of this Story.  # noqa: E501
        :rtype: int
        """
        return self._characters_count

    @characters_count.setter
    def characters_count(self, characters_count):
        """Sets the characters_count of this Story.

        Character count of the story body  # noqa: E501

        :param characters_count: The characters_count of this Story.  # noqa: E501
        :type characters_count: int
        """

        self._characters_count = characters_count

    @property
    def clusters(self):
        """Gets the clusters of this Story.  # noqa: E501

        An array of clusters the story is associated with  # noqa: E501

        :return: The clusters of this Story.  # noqa: E501
        :rtype: list[int]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this Story.

        An array of clusters the story is associated with  # noqa: E501

        :param clusters: The clusters of this Story.  # noqa: E501
        :type clusters: list[int]
        """

        self._clusters = clusters

    @property
    def entities(self):
        """Gets the entities of this Story.  # noqa: E501

        An array of entities  # noqa: E501

        :return: The entities of this Story.  # noqa: E501
        :rtype: list[Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this Story.

        An array of entities  # noqa: E501

        :param entities: The entities of this Story.  # noqa: E501
        :type entities: list[Entity]
        """

        self._entities = entities

    @property
    def hashtags(self):
        """Gets the hashtags of this Story.  # noqa: E501

        An array of suggested Story hashtags  # noqa: E501

        :return: The hashtags of this Story.  # noqa: E501
        :rtype: list[str]
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags):
        """Sets the hashtags of this Story.

        An array of suggested Story hashtags  # noqa: E501

        :param hashtags: The hashtags of this Story.  # noqa: E501
        :type hashtags: list[str]
        """

        self._hashtags = hashtags

    @property
    def id(self):
        """Gets the id of this Story.  # noqa: E501

        ID of the story which is a unique identification  # noqa: E501

        :return: The id of this Story.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Story.

        ID of the story which is a unique identification  # noqa: E501

        :param id: The id of this Story.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def keywords(self):
        """Gets the keywords of this Story.  # noqa: E501

        Extracted keywords mentioned in the story title or body  # noqa: E501

        :return: The keywords of this Story.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this Story.

        Extracted keywords mentioned in the story title or body  # noqa: E501

        :param keywords: The keywords of this Story.  # noqa: E501
        :type keywords: list[str]
        """

        self._keywords = keywords

    @property
    def language(self):
        """Gets the language of this Story.  # noqa: E501

        Language of the story  # noqa: E501

        :return: The language of this Story.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Story.

        Language of the story  # noqa: E501

        :param language: The language of this Story.  # noqa: E501
        :type language: str
        """

        self._language = language

    @property
    def links(self):
        """Gets the links of this Story.  # noqa: E501


        :return: The links of this Story.  # noqa: E501
        :rtype: StoryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Story.


        :param links: The links of this Story.  # noqa: E501
        :type links: StoryLinks
        """

        self._links = links

    @property
    def media(self):
        """Gets the media of this Story.  # noqa: E501

        An array of extracted media such as images and videos  # noqa: E501

        :return: The media of this Story.  # noqa: E501
        :rtype: list[Media]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this Story.

        An array of extracted media such as images and videos  # noqa: E501

        :param media: The media of this Story.  # noqa: E501
        :type media: list[Media]
        """

        self._media = media

    @property
    def paragraphs_count(self):
        """Gets the paragraphs_count of this Story.  # noqa: E501

        Paragraph count of the story body  # noqa: E501

        :return: The paragraphs_count of this Story.  # noqa: E501
        :rtype: int
        """
        return self._paragraphs_count

    @paragraphs_count.setter
    def paragraphs_count(self, paragraphs_count):
        """Sets the paragraphs_count of this Story.

        Paragraph count of the story body  # noqa: E501

        :param paragraphs_count: The paragraphs_count of this Story.  # noqa: E501
        :type paragraphs_count: int
        """

        self._paragraphs_count = paragraphs_count

    @property
    def published_datetime(self):
        """Gets the published_datetime of this Story.  # noqa: E501

        Publication time of the story, if available, otherwise time of acquisition  # noqa: E501

        :return: The published_datetime of this Story.  # noqa: E501
        :rtype: datetime
        """
        return self._published_datetime

    @published_datetime.setter
    def published_datetime(self, published_datetime):
        """Sets the published_datetime of this Story.

        Publication time of the story, if available, otherwise time of acquisition  # noqa: E501

        :param published_datetime: The published_datetime of this Story.  # noqa: E501
        :type published_datetime: datetime
        """

        self._published_datetime = published_datetime

    @property
    def published_at(self):
        """Gets the published_at of this Story.  # noqa: E501

        Acquisition time of the story  # noqa: E501

        :return: The published_at of this Story.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this Story.

        Acquisition time of the story  # noqa: E501

        :param published_at: The published_at of this Story.  # noqa: E501
        :type published_at: datetime
        """

        self._published_at = published_at

    @property
    def sentences_count(self):
        """Gets the sentences_count of this Story.  # noqa: E501

        Sentence count of the story body  # noqa: E501

        :return: The sentences_count of this Story.  # noqa: E501
        :rtype: int
        """
        return self._sentences_count

    @sentences_count.setter
    def sentences_count(self, sentences_count):
        """Sets the sentences_count of this Story.

        Sentence count of the story body  # noqa: E501

        :param sentences_count: The sentences_count of this Story.  # noqa: E501
        :type sentences_count: int
        """

        self._sentences_count = sentences_count

    @property
    def sentiment(self):
        """Gets the sentiment of this Story.  # noqa: E501


        :return: The sentiment of this Story.  # noqa: E501
        :rtype: Sentiments
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this Story.


        :param sentiment: The sentiment of this Story.  # noqa: E501
        :type sentiment: Sentiments
        """

        self._sentiment = sentiment

    @property
    def social_shares_count(self):
        """Gets the social_shares_count of this Story.  # noqa: E501


        :return: The social_shares_count of this Story.  # noqa: E501
        :rtype: ShareCounts
        """
        return self._social_shares_count

    @social_shares_count.setter
    def social_shares_count(self, social_shares_count):
        """Sets the social_shares_count of this Story.


        :param social_shares_count: The social_shares_count of this Story.  # noqa: E501
        :type social_shares_count: ShareCounts
        """

        self._social_shares_count = social_shares_count

    @property
    def source(self):
        """Gets the source of this Story.  # noqa: E501


        :return: The source of this Story.  # noqa: E501
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Story.


        :param source: The source of this Story.  # noqa: E501
        :type source: Source
        """

        self._source = source

    @property
    def summary(self):
        """Gets the summary of this Story.  # noqa: E501


        :return: The summary of this Story.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Story.


        :param summary: The summary of this Story.  # noqa: E501
        :type summary: Summary
        """

        self._summary = summary

    @property
    def title(self):
        """Gets the title of this Story.  # noqa: E501

        Title of the story  # noqa: E501

        :return: The title of this Story.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Story.

        Title of the story  # noqa: E501

        :param title: The title of this Story.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def translations(self):
        """Gets the translations of this Story.  # noqa: E501


        :return: The translations of this Story.  # noqa: E501
        :rtype: StoryTranslations
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this Story.


        :param translations: The translations of this Story.  # noqa: E501
        :type translations: StoryTranslations
        """

        self._translations = translations

    @property
    def words_count(self):
        """Gets the words_count of this Story.  # noqa: E501

        Word count of the story body  # noqa: E501

        :return: The words_count of this Story.  # noqa: E501
        :rtype: int
        """
        return self._words_count

    @words_count.setter
    def words_count(self, words_count):
        """Sets the words_count of this Story.

        Word count of the story body  # noqa: E501

        :param words_count: The words_count of this Story.  # noqa: E501
        :type words_count: int
        """

        self._words_count = words_count

    @property
    def license_type(self):
        """Gets the license_type of this Story.  # noqa: E501

        License type of the story  # noqa: E501

        :return: The license_type of this Story.  # noqa: E501
        :rtype: int
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this Story.

        License type of the story  # noqa: E501

        :param license_type: The license_type of this Story.  # noqa: E501
        :type license_type: int
        """

        self._license_type = license_type

    @property
    def industries(self):
        """Gets the industries of this Story.  # noqa: E501

        An array of industries categories  # noqa: E501

        :return: The industries of this Story.  # noqa: E501
        :rtype: list[Category]
        """
        return self._industries

    @industries.setter
    def industries(self, industries):
        """Sets the industries of this Story.

        An array of industries categories  # noqa: E501

        :param industries: The industries of this Story.  # noqa: E501
        :type industries: list[Category]
        """

        self._industries = industries

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
        if not isinstance(other, Story):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Story):
            return True

        return self.to_dict() != other.to_dict()
