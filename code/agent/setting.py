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

import os
import socket
import psutil

def get_ip_info():
	net_info = psutil.net_if_addrs()
	for item in net_info.items():
		if item[1][0].family == 2:
			address = item[1][0].address
	return address

SERVER = os.environ.get('SERVER_HOST',"localhost")
PORT = os.environ.get("PORT","5000")
ENDPOINT = get_ip_info()
TAGS = ["dev","sa"]

metric = {
    "metric":"",
    "endpoint":ENDPOINT,
    "tags":TAGS,
    "period":"",
    "value":"",
    "timestamp":"",
}

if __name__ == "__main__":
	print get_ip_info()
