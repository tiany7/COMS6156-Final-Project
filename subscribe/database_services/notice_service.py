import time

import couchdb

import os
import json
import middleware.context as context
class NoticeService:

    def __init__(self):
        pass

    @classmethod
    def get_connection(self, user_id):
        entry = couchdb.Server("http://admin:root@44.212.66.47:5984")
        db = None
        try:
            db = entry.create('hist/%s' % user_id)
        except:
            db = entry['hist/%s' % user_id]
        return db

    @classmethod
    def get_notice(self, user_id):
        db = self.get_connection(user_id)
        read, unread = None, None
        try:
            read = db['read']
            unread = db['unread']
        except:
            return {"status": "user not exists"}
        unread['history'] = sorted(unread['history'], key=lambda k: k['time'], reverse=True)
        read['history'] = sorted(read['history'], key=lambda k: k['time'], reverse=True)
        ret = unread['history']
        unread['history'] = []
        db.save(unread)
        db.save(read)
        return {"unread": ret}