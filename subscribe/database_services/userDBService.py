import couchdb

import os
import json
class UserDBService:

    def __init__(self):
        pass

    @classmethod
    def get_connection(self):
        entry = couchdb.Server("http://admin:root@44.212.66.47:5984")
        db = None
        try:
            db = entry.create('users')
        except:
            db = entry['users']

        return db

    @classmethod
    def create_user(self, user):
        db = self.get_connection()
        user["_id"] = user["user_id"]
        print(user)
        try:
            db.save(user)
            return None
        except:
            return {"status": "user already exists"}

    @classmethod
    def get_user(self, user_id):
        db = self.get_connection()
        user = db[user_id]
        return user

    @classmethod
    def get_user_by_email(self, email):
        db = self.get_connection()
        mango = {'selector': {'email': email}}
        for row in db.find(mango):
            return row
        return None

    @classmethod
    def get_user_by_name(self, name):
        db = self.get_connection()
        mango = {'selector': {'name': name}}
        for row in db.find(mango):
            return row
        return None

    @classmethod
    def get_user_by_id(self, user_id):
        db = self.get_connection()
        mango = {'selector': {'_id': user_id}}
        for row in db.find(mango):
            return row
        return None

    @classmethod
    def get_user_by_username(self, username):
        db = self.get_connection()
        mango = {'selector': {'username': username}}
        for row in db.find(mango):
            return row
        return None

