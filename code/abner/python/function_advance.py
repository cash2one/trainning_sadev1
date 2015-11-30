#-*- coding:utf-8 -*-

# def add(x,y):
    # return x+y
# # redecu 接受的函数只允许有两个参数
# print reduce(add,[1,2,3,4,5])

# def fn(x,y):
    # return 10*x+y

# def char2num(s):
    # return {
        # '0':0,
        # '1':1,
        # '2':2,
        # '3':3,
        # '4':4,
        # '5':5,
        # '6':6,
        # '7':7,
        # '8':8,
        # '9':9
    # }[s]
# finalint = reduce(fn,map(char2num,'13579'))
# print finalint

'''
def compare(a,b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
L = sorted([2,4,1,8,5,8,3,5])
print L

L = sorted([2,4,1,8,5,8,3,5],compare)
print L
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n;
        return ax
    return sum

#tips使用闭包的特性的时候就不要使用任何变化的量，延迟求值只会拿到变量最终的值
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i #i在此处是个外层函数的变量，在将函数加入数组的时候，并没有求值，但是变量i却一直在更新，所以最后所有的函数拿到的都是同一个i

        fs.append(f)
    return fs

def fun_close(x,y):
    return lambda :x*x + y*y #本质上也是闭包的一种形式，只不过使用了匿名函数


def log(func):
    print "log.name",log.__name__
    print "enter log"
    def wrapper(*args,**kw):
        print "wrapper.name", wrapper.__name__

        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print '2013-12-25'
'''
now()#这个时候调用now实际就是调用log函数修饰的新的now方法wrapper了，其实是把now函数作为参数传进log函数中
print now.__name__
'''

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)
            return  func(*args,**kw)
        return wrapper
    return decorator

