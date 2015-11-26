# -*- coding: utf-8 -*-
import psutil
import sys
import getopt
from time import sleep


class Agent(object):

    def __init__(self):
        self.argv = sys.argv[1:]
        self.DEFAULT_TIME = 1
        self.LOAD_DIR = '/proc/loadavg'

    def command(self, module, ttl):
        if not ttl:
            ttl = self.DEFAULT_TIME

        if module == 'all':
            self.loop_exec(ttl, self.get_load, self.get_cpu, self.get_memory)
        elif module == 'cpu':
            self.loop_exec(ttl, self.get_cpu)
        elif module == 'memory':
            self.loop_exec(ttl, self.get_memory)
        else:
            print 'option value error'
            sys.exit(1)

    def loop_exec(self, ttl, *func):
        while True:
            for f in func:
                f()
            sleep(ttl)

    def get_load(self):
        try:
            fd = open(self.LOAD_DIR, 'r')
            values = fd.readline().split(' ')[0:3]
            load_avg = {
                "w1_avg": values[0],
                "w5_avg": values[1],
                "w15_avg": values[2]
            }
            print "load_avg: ", load_avg
        except IOError as err:
            print err

    def get_cpu(self):
        cpu = psutil.cpu_times()
        if len(cpu) == 10:
            cpu_info = {
                "user": cpu.user,
                "nice": cpu.nice,
                "system": cpu.system,
                "idle": cpu.idle,
                "iowait": cpu.iowait,
                "irq": cpu.irq,
                "softtirq": cpu.softirq,
                "steal": cpu.steal,
                "guest": cpu.guest,
                "guest_nice": cpu.guest_nice
            }

            print "cpu_info: ", cpu_info

        else:
            print 'cpu_times length wrong'

    def get_memory(self):
        vir_mem = psutil.virtual_memory()
        swap_mem = psutil.swap_memory()
        mem_info = {
            "total": vir_mem.total,
            "used": vir_mem.used,
            "free": vir_mem.free,
            "buffers": vir_mem.buffers,
            "cached": vir_mem.cached,
            "active": vir_mem.active,
            "inactive": vir_mem.inactive,
            "swap_used": swap_mem.used,
            "abs_used": vir_mem.used - vir_mem.buffers - vir_mem.cached
        }
        print "mem_info: ", mem_info

    def show_version(self):
        print 'version 0.1'
        sys.exit()

    def show_help(self):
        print 'Usage: python agent.py [Options]'
        print "Options:"
        print "\t-v, --version\t\t show program version number and exit"
        print "\t-h, --help\t\t show this help message and exit"
        print "\t-t, --ttl\t\t set agent period, default is 60s"
        print "\t-m MODULE, --module=MODULE\t\t use module MODULE\n"
        print "Modules:"
        print "\tall, cpu, memory"
        sys.exit()

    def parse_args(self):
        try:
            opts, args = getopt.getopt(self.argv, "hvt:m:", ["help", "version", "ttl=", "module="])
        except getopt.GetoptError as err:
            print err
            self.show_help()
        module = ''
        ttl = ''
        for key, value in opts:
            if key == '-h':
                self.show_help()
            elif key == '-v':
                self.show_version()
            elif key in ('-m', '--module'):
                module = value
            elif key in ('-t', '--ttl'):
                ttl = value
            else:
                print "arguments error"
                self.show_help()
        return module, ttl


if __name__ == '__main__':
    agent = Agent()
    module, ttl = agent.parse_args()
    ttl = float(ttl)
    agent.command(module, ttl)
