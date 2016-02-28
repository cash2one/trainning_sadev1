# -*- coding:utf-8 -*-

import os

# mongodb config
MONGODB_DATABASE =  os.environ.get('MONGO_DATABASE', 'monitor-test')
MONGODB_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGODB_PORT = os.environ.get('MONGO_PORT', 27017)
MONGODB_USERNAME = None
MONGODB_PASSWORD = None


# 限制数据库返回数据
project = {
            "_id": 0,
            "endpoint": 0,
            "tags": 0,
            "metric": 0,
            "period": 0
        }
