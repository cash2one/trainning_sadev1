# -*- coding:utf-8 -*-
from flask.ext.restful import Resource
from flask import request
from flask import jsonify
from datetime import datetime

import app
from app.utils import request_parser
from config import project

categories = {
    'user': 0,
    'system': 1,
    'idle': 2,
    'nice': 3,
    'iowait': 4,
    'irq': 5,
    'softirq': 6,
    'steal': 7,
    'guest': 8,
    'guest_nice': 9
}


class CPU(Resource):
    def get(self):
        endpoint, _start, _end, category = request_parser(request)

        # 构造查询条件
        query = {
            "timestamp": {"$gt": _start, "$lt": _end},
            "endpoint": endpoint
        }

        cpus = app.db.CPU.find(query, project)
        data = list(cpus)

        # 格式化返回数据
        metric = {
            "categories": [],
            "series": [],
        }
        # 用于存储每次返回数据的横轴
        x_axis = []
        series = [
            {
                "name": "user",
                "data": []
            },
            {
                "name": "system",
                "data": []
            },
            {
                "name": "idle",
                "data": []
            },
            {
                "name": "nice",
                "data": []
            },
            {
                "name": "iowait",
                "data": []
            },
            {
                "name": "irq",
                "data": []
            },
            {
                "name": "softirq",
                "data": []
            },
            {
                "name": "steal",
                "data": []
            },
            {
                "name": "guest",
                "data": []
            },
            {
                "name": "guest_nice",
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
            series[3]['data'].append(item['value'][3])
            series[4]['data'].append(item['value'][4])
            series[5]['data'].append(item['value'][5])
            series[6]['data'].append(item['value'][6])
            series[7]['data'].append(item['value'][7])
            series[8]['data'].append(item['value'][8])
            series[9]['data'].append(item['value'][9])

        metric['categories'] = x_axis
        if category == 'all':
            metric['series'] = series
        else:
            metric['series'].append(series[categories[category]])

        return jsonify(metric)

    def post(self):
        # 获取请求中的数据, 这个api的返回值是dict,不是json,json是字符串
        data = request.json
        cpu = app.db.CPU(data)
        cpu.save()
        return "OK", 201
