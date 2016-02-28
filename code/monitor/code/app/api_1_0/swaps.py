# -*- coding:utf-8 -*-
from flask.ext.restful import Resource
from flask import request
from flask import jsonify
from datetime import datetime

import app
from app.utils import request_parser
from config import project

categories = {
    'total': 0,
    'used': 1,
    'free': 2,
}


class Swap(Resource):
    def get(self):
        endpoint, _start, _end, category = request_parser(request)

        # 构造查询条件
        query = {
            "timestamp": {"$gt": _start, "$lt": _end},
            "endpoint": endpoint
        }

        swaps = app.db.Swap.find(query, project)
        data = list(swaps)

        # 格式化返回数据
        metric = {
            "categories": [],
            "series": [],
        }
        # 用于存储每次返回数据的横轴
        x_axis = []
        series = [
            {
                "name": "total",
                "data": []
            },
            {
                "name": "used",
                "data": []
            },
            {
                "name": "free",
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
        swap = app.db.Swap(data)
        swap.save()
        return "OK", 201
