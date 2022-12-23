import json
import requests
import time
import datetime
import aylien_news_api
from aylien_news_api.rest import ApiException
import boto3

dynamodb = boto3.resource('dynamodb')
configuration = aylien_news_api.Configuration()

# Configure API key authorization: app_id
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'a4fb6cc0'

# Configure API key authorization: app_key
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '3ccc0581e25c7beae888989a888b5e5c'

# Defining host is optional and default to https://api.aylien.com/news
configuration.host = "https://api.aylien.com/news"
# Create an instance of the API class
api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))

opts = {
    'story_count_min': 123,
    'story_count_max': 1234,
    'time_start': 'NOW-3DAYS/DAY',
    'time_end': 'NOW-1DAY/DAY',
    }

subscription_key = ""
search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"

# es_endpoint = "https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com/news/_bulk"

# keys in each records that should be removed
def load_items(data):
    table = dynamodb.Table('6156-news')
    for item in data:
        # convert float to Decimal
        table.put_item(Item=item)

def extract_trending_topics():
    api_response = api_instance.list_clusters(**opts)
    print(api_response)
    # subscription_key = ""
    # search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"
    # headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    # params  = {"textDecorations": True, "textFormat": "HTML", "count": 100}
    # response = requests.get(search_url, headers=headers, params=params)
    # response.raise_for_status()
    # search_results = json.dumps(response.json())
    # results = response.json()
    # names = [article["name"] for article in results["value"]]
    
    return ""

def extract_news_contents(names):
    # Configure API key authorization: app_id
    configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'a4fb6cc0'

    # Configure API key authorization: app_key
    configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '3ccc0581e25c7beae888989a888b5e5c'

    # Defining host is optional and default to https://api.aylien.com/news
    configuration.host = "https://api.aylien.com/news"
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))
    
    url = "https://api.meaningcloud.com/deepcategorization-1.0"
    
    news = []

    x = datetime.datetime.now()
    try:
        # List Stories
        for topic in names:
            opts = {
                'title': topic,
                'published_at_start': 'NOW-1DAYS',
                'published_at_end': 'NOW',
                'language': ["en"],
                'sort_by': 'relevance',
                'per_page': 20
            }
            api_response = api_instance.list_stories(**opts)
            story = api_response.stories
            for s in story:
                new = {
                    "id": str(s.id),
                    "title": s.title,
                    "body": s.body,
                    "insert_time": str(x),
                }
                payload={
                    'key': '',
                    'txt': s.body,
                    'model': 'IAB_2.0_en',  # like IAB_2.0_en
                }
                response = requests.post(url, data=payload).json()
                # categories = s.keywords[:min(1, len(s.keywords))]
                # for cat in response['category_list']:
                #     categories.append(cat['label'].split(">")[0])
                # new['labels'] = categories
                news.append(new)
                
        return news
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)

def export_to_es(data):
    cnt = 0
    output = ""
    for n in data:
        for label in n['labels']:
            output += '{{ "index" : {{ "_index": "news", "_id" : "{}" }} }}\n'.format(cnt)
            output += '{{"id": "{}", "labels": "{}"}}\n'.format(n['id'], label)
            cnt += 1
    print(cnt)

    return json.dumps(output)

def lambda_handler(event, context):
    names = ["politics", "world cup", "education", "finance", "usa", "china", "sports", "new york", "art", "science", "liberty", "university"]
    news = extract_news_contents(names)
    print(news)
    load_items(news)
    # data = export_to_es(news)
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    # response = requests.post('https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com/news/_bulk', headers=headers, data=data, auth=('roy123', 'Ruoyu123#'))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
