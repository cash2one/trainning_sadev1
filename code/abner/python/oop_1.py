#! /usr/bin/env python
# -*- encoding:utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self._name = name
        self._score = score


    def __str__(self):
        return 'name:%s\tscore=%s' %(self._name,self._score)

    def __repr__(self):
        return 'name:%s\tscore=%s' %(self._name,self._score)

stu =  Student('alion',89)
print stu.name
