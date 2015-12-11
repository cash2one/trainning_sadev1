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
from psutil import swap_memory


def vir_mem_info():
    mem_monitor = virtual_memory()
    return {
        #前三个属性所有平台都有
        'total': mem_monitor.total,
        'available': mem_monitor.available,
        'used': mem_monitor.used,
        'free': mem_monitor.free,
        'percent': mem_monitor.percent,

        #可能会有些平台不提供下面的属性
        'active': mem_monitor.active \
        if hasattr(mem_monitor, 'active') else '',

        'inactive': mem_monitor.inactive\
        if hasattr(mem_monitor, 'inactive') else '',

        'buffers': mem_monitor.buffers \
        if hasattr(mem_monitor, 'buffers') else '',

        'cached': mem_monitor.cached  \
        if hasattr(mem_monitor, 'cached') else '',

        'wired': mem_monitor.wired \
        if hasattr(mem_monitor, 'wired') else '',

        'shared': mem_monitor.shared \
        if hasattr(mem_monitor, 'shared') else '',

    }


def swap_mem_info():
    swap_monitor = swap_memory()

    return {
        'total': swap_monitor.total,
        'used': swap_monitor.used,
        'free': swap_monitor.free,
        'percent': swap_monitor.percent,
        'sin': swap_monitor.sin,
        'sout': swap_monitor.sout,
    }


def monitor():
    return {
       'mem_vir_monitor': vir_mem_info(),
       'mem_swap_monitor': swap_mem_info()
        # 'timestamp':str(datetime.now())
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())

