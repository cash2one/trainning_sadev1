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

#命令行参数解析
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
                 Avaliable Modules:"
                 )


options,remainder = parse.parse_args(sys.argv[1:])
print options
