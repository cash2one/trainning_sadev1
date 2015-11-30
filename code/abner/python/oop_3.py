#! /usr/bin/env python
# -*- encoding:utf-8 -*-

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def next(self):
        self.a,self.b = self.b, self.a + self.b

        if self.a > 10000:
            raise StopIteration():
        return self.a

    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop

            a,b = 1,1
            L = []
            for x in range(stop):
                if x > start:
                    L.append(a)
                a,b = b,a+b
            return L

