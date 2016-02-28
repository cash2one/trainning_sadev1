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
from psutil import virtual_memory


def mem_info():
    mem_monitor = virtual_memory()
    return [
        mem_monitor.total,
        mem_monitor.used,
        mem_monitor.free,

        mem_monitor.shared \
        if hasattr(mem_monitor, 'shared') else 0,
         mem_monitor.buffers \
        if hasattr(mem_monitor, 'buffers') else 0,

        mem_monitor.cached  \
        if hasattr(mem_monitor, 'cached') else 0,


    ]



def monitor():
    return {
       'mem': mem_info(),
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())

