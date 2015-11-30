# -*- coding:utf-8 -*-

# 可变参数
def calc(*number):
    sum = 0
    print "sum",id(sum)
    print "number",type(number)

    for n in number:
        sum = sum + n*n
        print "sum",id(sum)

    return sum

# calc(1,2,3,4)
'''
output:
sum 140651064744448 输出sum的id只是为了继续帮助大家理解不可变对象
number <type 'tuple'> 从这个输出可以看出number实际是作为tuple传进来的，为什么不是list呢？继续理解不可变对象
sum 140651064744424
sum 140651064744328
sum 140651064744112
sum 140651064743728
'''

# 如果已经存在一个list或者tuple，那么应该怎么作为可变参数传递
# L = [1,2,3,4]
# calc(L) #此时L是作为可变参数传递进来的，而list的加法和整数的加法区别很大，得不到期望的结果
# calc(*L) #此时L就作为可变参数传进来了，其实这个操作和C语言中去指针中的数据很像。

# 关键字参数
def person(name, age, **kw):
    print 'kw',type(kw)
    print 'name:',name,'age:',age,'other:',kw

person('abner','22')
person('abner','22',city='Beijing')
'''
output:
    kw <type 'dict'> #关键字参数实际是作为一个字典的数据结构传进来的
name: abner age: 22 other: {}
kw <type 'dict'>
name: abner age: 22 other: {'city': 'Beijing'}
'''
# 如果事先存在一个字典可以通过类似于可变参数的方式把字典变成关键字参数
test_dict = {"city":"Beijing",
             "Tel":"185"
             }
person("abner","22",**test_dict)
