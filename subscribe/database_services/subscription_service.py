import time

import couchdb

import os
import json
import middleware.context as context
import middleware.sns as sns
import boto3
sns_wrapper = sns.SnsWrapper(boto3.resource('sns', region_name='us-east-1', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_ACCESS_KEY']))
class SubscriptionService:

    def __init__(self):
        pass

    @classmethod
    def get_connection(self):
        entry = couchdb.Server("http://admin:root@44.212.66.47:5984")
        db = None
        try:
            db = entry.create('subscriptions')
        except:
            db = entry['subscriptions']

        return db

    @classmethod
    def get_history_db(self, user_id):
        entry = couchdb.Server("http://admin:root@44.212.66.47:5984")
        db = None
        try:
            db = entry.create('hist/%s' % user_id)
        except:
            db = entry['hist/%s' % user_id]
        return db

    @classmethod
    def create_user_record(self, user_id, email=None):
        db = self.get_connection()
        print(user_id)
        try:
            db.save({'_id': user_id, 'subscriptions': [], 'subscribers': []})
        except:
            return {"status": "user already exists"}
        mdb = self.get_history_db(user_id)
        topic_name = f'our-demo'
        topic = sns_wrapper.create_topic(topic_name)
        email_sub = sns_wrapper.subscribe(topic, 'email', email)
        print(email)

        try:
            mdb.save({'_id': 'read', 'history': []})
            mdb.save({'_id': 'unread', 'history': []})
        except:
            return {"status": "user already exists"}
        return None

    @classmethod
    def create_subscription(self, from_user, to_user):
        db = self.get_connection()
        subscriber_record = None
        subscribed_record = None
        try:
            subscriber_record = db[from_user]
            print(subscriber_record)
            if to_user in subscriber_record["subscriptions"]:
                return {"status": "already subscribed"}
            subscriber_record["subscriptions"].append(to_user)
        except Exception as e:
            print('exception', e)
            return {"status": "user not found"}

        try:
            subscribed_record = db[to_user]
            if from_user in subscribed_record["subscribers"]:
                return {"status": "already subscribed"}
            subscribed_record["subscribers"].append(from_user)
        except:
            return {"status": "user not found"}
        self.add_history(from_user, to_user, "subscribe")
        db.update([subscriber_record, subscribed_record])
        return None

    @classmethod
    def unsubscribe(self, from_user, to_user):
        db = self.get_connection()
        subscriber_record = None
        subscribed_record = None
        try:
            subscriber_record = db[from_user]
            if to_user not in subscriber_record["subscriptions"]:
                return {"status": "not subscribed"}
            subscriber_record["subscriptions"].remove(to_user)
        except:
            return {"status": "user not found"}

        try:
            subscribed_record = db[to_user]
            if from_user not in subscribed_record["subscribers"]:
                return {"status": "not subscribed"}



            subscribed_record["subscribers"].remove(from_user)
        except:
            return {"status": "user not found"}
        self.add_history(from_user, to_user, "unsubscribe")
        db.update([subscriber_record, subscribed_record])
        return None

    @classmethod
    def get_subscribers(self, user_id, start=0, count=10):
        db = self.get_connection()
        if start is None:
            start = int(0)
            count = int(10)
        try:
            record = db[user_id]
            print(type(record["subscribers"]))
            tot = 0
            start = int(start)
            count = int(count)
            return record["subscribers"][start:start + count]
        except Exception as e:
            print(e)
            return {"status": "user not found"}


    @classmethod
    def get_subscribed(self, user_id, start=0, count=10):
        db = self.get_connection()
        if start is None:
            start = 0
            count = 10
        try:
            record = db[user_id]
            start = int(start)
            count = int(count)
            print(type(record["subscriptions"]))
            return record["subscriptions"][start:start+count]
        except Exception as e:
            print(e)
            return []

    @classmethod
    def get_history(self, user_id, start, offset):
        db = self.get_history_db(user_id)
        history = []
        for row in db.view('_all_docs', limit=offset, skip=start):
            history.append(db[row.id])
        return history

    @classmethod
    def add_history(self, from_user, to_user, type):
        db = self.get_history_db(to_user)
        unread = db['unread']
        unread['history'].append({'from': from_user, 'time': time.time(), 'type': type})
        db.update([unread])
        return None