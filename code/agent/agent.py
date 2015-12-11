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

import optparse
import sys
import logging
import time
import sched
import plugins
from pprint import pprint


class Agent(object):

    def __init__(self):
        self.argv = sys.argv[1:]

    def parse_args(self):
        parse = optparse.OptionParser()
        parse.add_option(
            '-v', '--version',
            action='store_true',
            default=False,
            dest='version',
            help='show program number and exit.',
        )
        parse.add_option(
            '-t', '--ttl',
            action='store',
            dest='ttl',
            default='1',
            help='set agent period,default is 60s',
        )
        parse.add_option(
            '-m', '--module',
            action='store',
            dest='module',
            default='all',
            help="set module MODULE ,default output all modules.\n \
                Avaliable Modules:cpu,memory,load"
        )
        options, remainder = parse.parse_args(self.argv)
        if options.version:
            self.show_version()
            sys.exit(0)

        if options.ttl:
            try:
                int(options.ttl)
            except ValueError:
                logging.error('the value of ttl must be a postive integer!!!')
                exit(-1)

        if options.module not in plugins.monitor.keys()+['all']:
            logging.warning('Invalid module,avaliable modules are {cpu,memory,load,all}')
            exit(-1)
        else:
            return int(options.ttl), options.module

    def show_version(self):
        print 'Agent:1.0'
        sys.exit(0)

    # 监控任务
    def run_monitor(self, module):
        monitor = plugins.monitor
        if module == 'all':
            for key in monitor.keys():
                pprint(monitor[key]())
        else:
            pprint(monitor[module]())

    def work_schedule(self, ttl, module):
        while True:
            s = sched.scheduler(time.time, time.sleep)
            s.enter(ttl, 0, self.run_monitor, (module,))
            s.run()


if __name__ == '__main__':
    agent = Agent()
    ttl, module = agent.parse_args()
    agent.work_schedule(ttl, module)
