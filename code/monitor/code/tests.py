# -*- coding:utf-8 -*-

import unittest
from app import app, db
import json


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        '''
        self.app_context = self.app.app_context()
        self.app_context.push()
        '''

    def tearDown(self):
        pass
        '''
        self.app_context.pop()
        '''

    def test_models_load_write(self):
        with app.app_context():
            data = {
                "metric": u"load",
                "endpoint": u"localhost",
                "timestamp": 123456789,
                "tags": [u"dev", u"sa"],
                "period": 60,
                "value": [1.2, 1.3, 1.4]
            }
            json_data = json.dumps(data)
            # 以字典的形式初始化
            # load = db.Load(data)
            # 以json的形式初始化
            load = db.Load.from_json(json_data)
            load.save()

    def test_models_load_read(self):
        with app.app_context():
            loads = db.Load.find({}, {'_id': 0})
            print list(loads)

    def test_models_mem(self):
        with app.app_context():
            data = {
                "metric": u"mem",
                "endpoint": u"localhost",
                "timestamp": 123456789,
                "tags": [u"dev", u"sa"],
                "period": 60,
                "value": [49555412, 15670092, 33885320, 992540, 576075, 14022700]
            }
            json_data = json.dumps(data)
            mem = db.Mem.from_json(json_data)
            mem.save()

    def test_models_swap(self):
        with app.app_context():
            data = {
                "metric": u"mem",
                "endpoint": u"localhost",
                "timestamp": 123456789,
                "tags": [u"dev", u"sa"],
                "period": 60,
                "value": [4149300, 0, 4149300]
            }
            json_data = json.dumps(data)
            swap = db.Swap.from_json(json_data)
            swap.save()

    def test_models_cpu(self):
        with app.app_context():
            data = {
                "metric": u"mem",
                "endpoint": u"localhost",
                "timestamp": 123456789,
                "tags": [u"dev", u"sa"],
                "period": 60,
                "value": [0.19, 0.00, 0.43, 0.06, 0.00, 99.33, 0.00, 0.00, 0.00, 0.00]
            }
            json_data = json.dumps(data)
            cpu = db.CPU.from_json(json_data)
            cpu.save()


if __name__ == "__main__":
    unittest.main()
