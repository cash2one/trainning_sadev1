#! /usr/bin/env python
# -*- encoding:utf-8 -*-
class Student(object):
    pass

s = Student()
s.name = 'Abner' #动态绑定
print s.name

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Student) #动态绑定方法,仅仅绑定到当前实例

s.set_age(25)
s.age

def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score,None,Student)#将方法绑定到类上。

#由上面可以看出，Python中的类的属性是动态变化的，这样太随意会导致类的实例的状态不可控
#可以通过__slots__限制可以动态添加的属性，但是还是很不建议修改类的属性
class Student(object):
    __slots__ = ('name','age')#只允许给类添加这两个属性

