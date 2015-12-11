#! /usr/bin/env python
# -*- encoding:utf-8 -*-
'''
FileName: stage1_agent.py
Author: Abner Kang
@contact:gzkangjinglong@corp.netease.com
@version:1.0
Description:
Changelog:
'''
from psutil import cpu_times_percent
from datetime import datetime

def cpu_info():
     cpu_monitor = cpu_times_percent()
     return {
        #前三个属性所有平台都有
        'user':cpu_monitor.user,
        'system':cpu_monitor.system,
        'idle':cpu_monitor.idle,

        #可能会有些平台不提供下面的属性
        'nice':cpu_monitor.nice \
        if hasattr(cpu_monitor,'nice') else '',

        'iowait':cpu_monitor.iowait\
        if hasattr(cpu_monitor,'iowait') else '',

        'irq':cpu_monitor.irq \
        if hasattr(cpu_monitor,'irq') else '',

        'softirq':cpu_monitor.softirq  \
        if hasattr(cpu_monitor,'softirq') else '',

        'steal':cpu_monitor.steal \
        if hasattr(cpu_monitor,'steal') else '',

        'guest':cpu_monitor.guest \
        if hasattr(cpu_monitor,'guest') else '',

        'guest_nice':cpu_monitor.guest_nice \
        if hasattr(cpu_monitor,'guest_nice') else '',
    }

def monitor():
    return {
        'cpu_monitor':cpu_info(),
        'timestamp':str(datetime.now()),
    }
if __name__ == '__main__':
    from pprint import pprint

    pprint(monitor())

