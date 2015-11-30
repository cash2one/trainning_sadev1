# -*- encoding:utf-8 -*-
import functools

def log(func):
    def wrapper(*args,**kw):
        print 'Before call %s' %(func.__name__)
        return func(*args,**kw)#这里返回的是函数的执行结果，此处函数已经执行，不存在延迟加载
    #上面仅仅就是定义了一个函数，这个函数不调用的话是不会执行的，所以考虑这个执行顺序的话可以不看上面的

    print 'End call %s' %(func.__name__)
    return wrapper

def log_args(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s Before call %s' %(text,func.__name__)
            return func(*args,**kw) #这里返回的已经是函数的调用结果，在此处是没有延迟执行的
        print 'End call %s' %(func.__name__)

        return wrapper#这里返回的是函数
    return decorator#这里返回的也是函数



@log_args('hello')
def now():
    print '2015-11-28'

now()#实际是将now作为参数传进了log，返回了wrapper，此时now.__name__ == wrapper
