#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""
FileName: memory.py
Author: Abner Kang
@contact:gzkangjinglong@corp.netease.com
@version:1.0
Description:
Changelog:
"""
from psutil import swap_memory

def swap_info():
    swap_monitor = swap_memory()

    return [
        swap_monitor.total,
        swap_monitor.used,
        swap_monitor.free,
    ]


def monitor():
    return {
       'swap': swap_info()
        # 'timestamp':str(datetime.now())
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())

