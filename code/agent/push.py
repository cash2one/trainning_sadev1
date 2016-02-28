#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""
FileName: push.py
Author: Abner Kang
@contact:gzkangjinglong@corp.netease.com
@version:1.0
Description:
Changelog:
"""

import json
import requests
from pprint import pprint
def push(url,data):
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url,json.dumps(data),headers=headers)

    pprint(resp.json())

