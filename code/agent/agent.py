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
import os
import sys
import logging

import plugins

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

if __name__ == '__main__':
    from pprint import pprint

    options,remainder = parse_args().parse_args(sys.argv[1:])

    cpu_monitor = plugins.cpu.monitor
   #  load_monitor = plugins.load.monitor
    # memory_monitor = plugins.memory.monitor

    monitors = {'cpu':cpu_monitor,}

    if options.version:
        print 'Agent:1.0'
        sys.exit(0)

    if options.ttl:
        try:
            int(options.ttl)
        except ValueError:
            logging.error('the value of ttl must be a postive integer!!!')
            exit(-1)

    if options.module not in ['cpu','memory','load','all']:
        logging.warning('Invalid module,avaliable modules are cpu,memory,load,all')
        exit(-1)
    elif options.module == 'cpu':
        pprint(monitors['cpu']())
    else:
        pass

