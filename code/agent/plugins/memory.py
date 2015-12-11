#! /usr/bin/env python
# -*- encoding:utf-8 -*-
'''
FileName: memory.py
Author: Abner Kang
@contact:gzkangjinglong@corp.netease.com
@version:1.0
Description:
Changelog:
'''
from psutil import virtual_memory

def monitor():
     mem_monitor = virtual_memory()
     return {
        #前三个属性所有平台都有
        'total':mem_monitor.total,
        'available':mem_monitor.available,
        'used':mem_monitor.used,
        'free':mem_monitor.free,
        'percent':mem_monitor.percent,

        #可能会有些平台不提供下面的属性
        'active':mem_monitor.active \
        if hasattr(mem_monitor,'active') else '',

        'inactive':mem_monitor.inactive\
        if hasattr(mem_monitor,'inactive') else '',

        'buffers':mem_monitor.buffers \
        if hasattr(mem_monitor,'buffers') else '',

        'cached':mem_monitor.cached  \
        if hasattr(mem_monitor,'cached') else '',

        'wired':mem_monitor.wired \
        if hasattr(mem_monitor,'wired') else '',

        'shared':mem_monitor.shared \
        if hasattr(mem_monitor,'shared') else '',

    }


if __name__ == '__main__':
    print monitor()

