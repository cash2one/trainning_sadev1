#-*- coding:utf8 -*-
'''
根据下面的测试用例好好理解什么是可变对象，是么是不可变对象，copy-on-write
为什么跟C语言的局部变量差距这么大？
其实，所做的一切工作都是动态语言对了优化内存的使用而做的，所以不可变对象是所有动态语言的共性。
因为动态语言没有编译的过程，为了简单基本都采用了不可变对象的设计思路，一定要理解不可变的到底是什么。
不可变对象带来的另一个好处就是在多线程条件下，就不需要锁机制了，既然不能变，大家看到的都一样。
'''
def add_end(L=[]):
    print "add_end:",id(L)
    L.append('END')
    return L

def add_end_2():
    L = []
    print "L",id(L)
    L.append("END")
    return L

def add_int():
    a = 1
    print "a",id(a)
    return a

def add_int_2():
    a = 1
    print "a",id(a)
    return a+1

# final testcase:是不是跟你想的不一样，看懂这个终极用例，就完全理解不可变对象了

'''
 >>> a = 1
 >>> id(a)
 140519548175368
 >>> a = a+1
 >>> id(a)
 140519548175344

'''


# testcase 005
b = add_int_2()
print "b",id(b)

'''
a 140534715799624
b 140534715799600
'''


# testcase 004
# b = add_int()
# print "b",id(b)
'''
output:
    a 140642114127672
    b 140642114127672
'''


# testcase 003
# M = add_end_2()
# print "M",id(M)
'''
output:
    L 4543486648
    M 4543486648
'''

# testcase 001
# L = [1,2,3]
# print "main:",id(L)

# M = add_end(L)

# print "main:M:",id(M)

'''
output:
    main: 4550744760
    add_end: 4550744760
    main:M: 4550744760
'''

#testcase 002

# M = add_end()
# print 'M',id(M)
# print M


# M = add_end()
# print 'M',id(M)
# print M


'''
add_end: 4558440568
M 4558440568
['END']
add_end: 4558440568
M 4558440568
['END', 'END']
'''

