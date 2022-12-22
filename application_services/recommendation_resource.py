from abc import ABC

from application_services.BaseApplicationResource import BaseRDBApplicationResource
import os
import boto3
import requests
import json
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
        news_info = dynamodb.Table("6156-news")
        # rds = boto3.client('rds', aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        #                    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        #                    region_name='us-east-2')

        return news_info

    @staticmethod
    def get_by_page_id(page_id, page_num=10):
        page_id = int(page_id)
        news_info = RecommendationResource._get_connection().scan()["Items"]
        like_dislike = []

        for item in news_info[:10]:
            cur_news = json.loads(requests.get(f"https://7k9oonv11m.execute-api.us-east-1.amazonaws.com/Prod/news?NewsID={item['id']}").text)
            like_dislike.append({
                "id": item["id"],
                "title": item["title"],
                "body": item["body"],
                "like": cur_news["Likes"],
                "dislike": cur_news["Disikes"],
                "real_like": cur_news["Likes"]-cur_news["Disikes"],
            })

        top_k = sorted(like_dislike, key=lambda k: k['real_like'])
        response = []
        for top_k_id in range(page_num*(page_id-1), page_id*page_num):
            response.append({
                "id": top_k[top_k_id]["id"],
                "title": top_k[top_k_id]["title"],
                "body": top_k[top_k_id]["body"],
                "like": top_k[top_k_id]["like"],
                "dislike": top_k[top_k_id]["dislike"],
            })

        return response
