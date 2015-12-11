# -*- coding: utf-8 -*-
from datetime import datetime
def load_info():
    return {
        'w1_avg':'0.0',
        'w2_avg':'0.0',
        'w3_avg':'0.0',
        # 'timestamp':str(datetime.now()),
    }

def monitor():
    return {
        'load_monitor':load_info(),
        'timestamp':str(datetime.now()),
    }



if __name__ == '__main__':
    from pprint import pprint
    pprint(monitor())
