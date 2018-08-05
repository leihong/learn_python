#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 2000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片, 这里只实现 step=1的切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    if n < 20:
        print(n)
print('fib[1]=',Fib()[10])
print('fib[:5]', Fib()[:5])

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        #if path == 'users':
         #   return lambda x : Chain('%s/%s:%s' % (self._path,path,x))
        if path=='users':
            return lambda x: Chain('%s/%s/%s' % (self._path, path, x))
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return 'Chain is: ' +  self._path

    __repr__ = __str__

s = Chain('/usr')
s
print(s.test.mm)
print(Chain().users('michael').repos)
