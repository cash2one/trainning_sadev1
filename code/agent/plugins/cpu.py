#! /usr/bin/env python
# -*- encoding:utf-8 -*-
"""
FileName: stage1_agent.py
Author: Abner Kang
@contact:gzkangjinglong@corp.netease.com
@version:1.0
Description:
Changelog:
"""
from psutil import cpu_times


def cpu_info():
    cpu_monitor = cpu_times()
    cpu_total = cpu_monitor.user + cpu_monitor.system + cpu_monitor.idle \
        + cpu_monitor.nice + cpu_monitor.iowait + cpu_monitor.irq + \
        cpu_monitor.softirq + cpu_monitor.steal + cpu_monitor.guest +\
        cpu_monitor.guest_nice

    return [
        round(cpu_monitor.user/cpu_total,2),
        round(cpu_monitor.system/cpu_total,2),
        round(cpu_monitor.idle/cpu_total,2),

        round(cpu_monitor.nice/cpu_total,2) \
        if hasattr(cpu_monitor, 'nice') else 0.0,

        round(cpu_monitor.iowait/cpu_total,2)\
        if hasattr(cpu_monitor, 'iowait') else 0.0,

        round(cpu_monitor.irq/cpu_total,2) \
        if hasattr(cpu_monitor, 'irq') else 0.0,

        round(cpu_monitor.softirq/cpu_total,2)  \
        if hasattr(cpu_monitor, 'softirq') else 0.0,

        round(cpu_monitor.steal/cpu_total,2) \
        if hasattr(cpu_monitor, 'steal') else 0.0,

        round(cpu_monitor.guest/cpu_total,2) \
        if hasattr(cpu_monitor, 'guest') else 0.0,

        round(cpu_monitor.guest_nice/cpu_total,2) \
        if hasattr(cpu_monitor, 'guest_nice') else 0.0,
    ]


def monitor():
    return {
        'cpu': cpu_info()
        # 'timestamp':str(datetime.now()),
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())

