# 6156 Final Project: Daily News Notifications

## Team
Dengpan Yuan: dy2436

## Goal
Build up a system can support: 
- Subscription Service + Notification/Push Service  Owner: [Owner: Yuanhan Tian]
- Comment Service -> CRUD [Owner: Jiming Yu] comment-api link: https://xbo0hw7f2k.execute-api.us-east-1.amazonaws.com/comment_news/message
- Like/Dislike Service  [Owner: Jack Wang] 
- Article Base Service  [Owner: Yilin Li]
- Recommender Service  [Owner: Weichen Li]
- Search Service ->CRUD [Owner: Dengpan Yuan]
- OAuth2 Service： [Owner: Hangpu Cao]

## Useful Resource
Github Repo: 
  - https://github.com/tiany7/COMS6156-Sprint1-Repo1 
  - https://github.com/tiany7/COMS6156-Sprint1-Repo2
  - https://github.com/tiany7/COMS6156-Sprint1-Repo3


Trello:
- https://trello.com/b/y0iFXwOU/cs6156-sprint-1

SNS:
- https://us-east-1.console.aws.amazon.com/sns/v3/home?region=us-east-1#/dashboard



News API:
- https://aylien.com/product/news-api

Google Doc Sprint:
- https://docs.google.com/document/d/1HWu0sCU6g2u53KAK781sMs6Sw9DCXxS9MvQyUPr6UFA/edit

Demo Slides
- https://docs.google.com/presentation/d/1KUbxh3La3HDYr-s0N6dRKhm_1szxVRnJFiiIZrE4p3Y/edit?usp=sharing

Retool
- https://tiany7.retool.com/editor/e11b04e6-7da1-11ed-8f67-7743436a77a8/coms6156

## Implemetation

### Search
A context search functionality build by tf-idf and lsi, which can recommend most top similar n news from database providing the search keyword. 

### Subscribe/Unsubscribe
A functionality that allows the user to subscribe/unsubscribe other users. It also provides user the APIs to get the list of subscriptions, fans and activity histories. 
