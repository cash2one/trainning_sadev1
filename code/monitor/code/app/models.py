# -*- coding:utf-8 -*-
from flask.ext.mongokit import Document
from app import db


@db.register
class Load(Document):
    __collection__ = 'loads'
    structure = {
        "metric": unicode,
        "endpoint": unicode,
        "timestamp": int,
        "period": int,
        "tags": [unicode],
        "value": [float],  # 1min,10min,15min
    }

    use_dot_notation = True


@db.register
class Mem(Document):
    __collection__ = 'mems'
    structure = {
        "metric": unicode,
        "endpoint": unicode,
        "timestamp": int,
        "period": int,
        "tags": [unicode],
        "value": [int],  # total,used, free, shared, buffers,cached
    }

    use_dot_notation = True


@db.register
class Swap(Document):
    __collection__ = 'swaps'
    structure = {
        "metric": unicode,
        "endpoint": unicode,
        "timestamp": int,
        "period": int,
        "tags": [unicode],
        "value": [int],  # total, used, free
    }
    use_dot_notation = True


@db.register
class CPU(Document):
    __collection__ = 'cpus'
    structure = {
        "metric": unicode,
        "endpoint": unicode,
        "timestamp": int,
        "period": int,
        "tags": [unicode],
        # user, nice, system, iowait, steal, idle, irq, softirq, guest, guest_nice
        "value": [float],

    }
    use_dot_notation = True
