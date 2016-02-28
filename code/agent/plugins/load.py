# -*- coding: utf-8 -*-

LOAD_PATH = '/proc/loadavg'


def load_info():
    try:
        fd = open(LOAD_PATH, 'r')
        values = fd.readline().split(' ')[0:3]
        # 1min, 10min, 15min
        load_avg = [float(values[0]), float(values[1]), float(values[2])]
        return load_avg
    except IOError as err:
        print err
    finally:
        if 'fd' in locals():
            fd.close()


def monitor():
    # 后面要判断是否读取文件成功，若open失败，'load_monitor'的value为None
    return {
        'load': load_info()
        # 'timestamp': str(datetime.now()),
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())
    print monitor()['load']['1min']
