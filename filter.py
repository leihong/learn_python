#!/usr/bin/env python3
#coding=utf-8


#filter's return is an Iterater
def not_empty(s):
    return s and s.strip()
L=list(filter(not_empty, ['A', 'B', 'AB C', None, 'C', ' ']))
print(L)

def isodd(n):
    return n % 2 == 1

L=list(filter(isodd, [1,2,4,5,6,9,10,333]))
print(L)

#primer achivement
def _odd_iter():
    n=1
    while True:
        n = n + 2
        print('T:', n)
        yield n

#lambda is an anonymous function
def not_divisible(n):
    return lambda x: x% n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)

# this function can only be run on python 3
for n in primes():
    if n < 10:
        print(n)
    else:
        break

def is_palindrome(n):
    s = str(n)
    #s[::-1] reverse s
    return s==s[::-1]

P=filter(is_palindrome, range(1,1000))
print('1~1000:', list(P))

#split
# start_index ~ end_index's direction should same as step's direction
# otherwise will generate a empty List
C='123456'

# start_index ~ end_index is +, but step is - , will get empty str
L=C[0:3:-1]
print('F:', L)

# start_index ~ end_index is -, but step is +, will get empty str
L=C[3:0:1]
print('F:', L)

# start_index ~ end_index is -, but step is +(default is +1) , will get empty str
L=C[3:0:]
print('F:', L)

# start_index ~ end_index is +, and step is +(default is +1) , will get str
L=C[0:3:1]
print('T:', L)

L=C[::-1]
print('Reverse List:', L)

L=C[:]
print('Reverse List:', L)

L=C[::]
print('Reverse List-1:', L)

L=C[::1]
print('Reverse List-2:', L)
