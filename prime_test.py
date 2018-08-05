#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

def odd_iter():
    i=1
    while True:
        i += 2
        yield i

def not_divisable(n):
    return lambda x: x%n!=0

def prime_iter():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisable(n), it)
        #it = filter(lambda x:x%3!=0, it)
L=[]
count=0
for n in prime_iter():
    if n>50:
        break
    L.append(n)
    count += 1

print('prime count in range(0~50): %d, sum:%d' % (count, sum(L)))
print('prime List:', L)
    
