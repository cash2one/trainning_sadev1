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

import optparse
import sys
import logging
import time
import sched

import plugins
from pprint import pprint


#命令行参数解析
def parse_args():
    parse = optparse.OptionParser()

    parse.add_option('-v','--version',
                     action = 'store_true',
                    default = False,
                    dest = 'version',
                    help = 'show program number and exit.',
                    )

    parse.add_option('-t','--ttl',
                     action = 'store',
                     dest = 'ttl',
                     default = '60',
                     help = 'set agent period,default is 60s',
                     )
    parse.add_option('-m','--module',
                     action = 'store',
                     dest = 'module',
                     default = 'all',
                     help = "set module MODULE ,default output all modules.\n \
                    Avaliable Modules:cpu,memory,load"
                    )
    return parse

def show_version():
    print 'Agent:1.0'
    sys.exit(0)

# 监控任务
def run_monitor(module):
    monitor = plugins.monitor
    if module == 'all':
        for key in monitor.keys():
            pprint(monitor[key]())
    else:
        pprint(monitor[module]())


#任务调度器
s = sched.scheduler(time.time,time.sleep)
def perform(ttl,module):
    s.enter(ttl,0,perform,(ttl,module))
    run_monitor(module)

def work_shedule(ttl,module):
    s.enter(0,0,perform,(ttl,module))
    s.run()

if __name__ == '__main__':

    options,remainder = parse_args().parse_args(sys.argv[1:])

    if options.version:
        show_version()
        sys.exit(0)

    if options.ttl:
        try:
            int(options.ttl)
        except ValueError:
            logging.error('the value of ttl must be a postive integer!!!')
            exit(-1)

    if options.module not in ['cpu','memory','load','all']:
        logging.warning('Invalid module,avaliable modules are {cpu,memory,load,all}')
        exit(-1)
    else:
        work_shedule(int(options.ttl),options.module)
        sys.exit(0)

