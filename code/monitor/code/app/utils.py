# -*- coding:utf-8 -*-
from flask import jsonify


def request_parser(request):
    endpoint = request.args.get("endpoint", "")  # string
    _start = request.args.get("_start", "")
    _end = request.args.get("_end", "")
    category = request.args.get("category", "all")

    return endpoint, int(_start), int(_end), category
