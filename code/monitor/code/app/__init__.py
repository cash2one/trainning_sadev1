# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.mongokit import MongoKit
from flask.ext.restful import Api

from . api_1_0 import loads, mems, swaps, cpus

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

# 添加路由
api.add_resource(loads.Load, '/api/v1/loads')
api.add_resource(mems.Mem, '/api/v1/mems')
api.add_resource(swaps.Swap, '/api/v1/swaps')
api.add_resource(cpus.CPU, '/api/v1/cpus')

# 初始化数据库
db = MongoKit(app)

from . import models, utils

