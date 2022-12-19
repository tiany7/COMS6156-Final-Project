from abc import ABC

from application_services.BaseApplicationResource import BaseRDBApplicationResource
import os
import boto3
from boto3.dynamodb.conditions import Key


class RecommendationResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
                                  aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
                                  region_name='us-east-1')
        news_info = dynamodb.Table("news")
        news_likes = dynamodb.Table("news_like_dislike")
        # rds = boto3.client('rds', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        #                    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        #                    region_name='us-east-2')

        return news_likes, news_info

    @staticmethod
    def get_by_page_id(key):
        print("In Recommendation!")
        news_likes, news_info = RecommendationResource._get_connection()
        top_k = news_likes.scan()['Items']
        top_k = sorted(top_k, key=lambda k: k['likes'])
        print(top_k)
        response = []
        for news in top_k:
            news_id = news['news_id']
            print(news_id)
            response.extend(news_info.query(
                KeyConditionExpression=Key('news_id').eq(news_id)
            )['Items'])
        print(response)

        return response
