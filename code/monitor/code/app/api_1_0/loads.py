# -*- coding:utf-8 -*-
from flask.ext.restful import Resource
from flask import request
from flask import jsonify
from datetime import datetime

import app
from app.utils import request_parser
from config import project

categories = {
    'w1': 0,
    'w5': 1,
    'w15': 2,
}


class Load(Resource):
    def get(self):
        endpoint, _start, _end, category = request_parser(request)

        # 构造查询条件
        query = {
            "timestamp": {"$gt": _start, "$lt": _end},
            "endpoint": endpoint
        }

        loads = app.db.Load.find(query, project)
        data = list(loads)

        # 格式化返回数据
        metric = {
            "categories": [],
            "series": [],
        }
        # 用于存储每次返回数据的横轴
        x_axis = []
        series = [
            {
                "name": "w1",
                "data": []
            },
            {
                "name": "w5",
                "data": []
            },
            {
                "name": "w15",
                "data": []
            }
        ]

        for item in data:
            format_time = datetime.fromtimestamp(item['timestamp'])\
                .strftime("%Y-%m-%d %H:%M:%S")
            x_axis.append(format_time)
            series[0]['data'].append(item['value'][0])
            series[1]['data'].append(item['value'][1])
            series[2]['data'].append(item['value'][2])

        metric['categories'] = x_axis
        if category == 'all':
            metric['series'] = series
        else:
            metric['series'].append(series[categories[category]])

        return jsonify(metric)

    def post(self):
        # 获取请求中的数据, 这个api的返回值是dict,不是json
        data = request.json
        load = app.db.Load(data)
        load.save()

        return "OK", 201

