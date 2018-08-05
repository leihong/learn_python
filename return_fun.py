#!/usr/bin/env python3

def lazy_sum(*args):
    def sum():
        my_sum=0
        for i in args:
            my_sum += i
        return my_sum
    return sum

f=lazy_sum(1,2,3,4,5)
s=f()
print(s)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
i=10
print(f1())
print(f2())
print(f3())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
