# -*- coding: utf-8 -*-
import cpu
import mem
import swap
import load

monitor = {
    'cpu': cpu.monitor,
    'mem': mem.monitor,
    'swap':swap.monitor,
    'load': load.monitor,
}
