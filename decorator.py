#!/usr/bin/env python3

print('\n\ntest0:')
def now():
    print('now')

f=now
f()
print(f.__name__)
print(now.__name__)


print('\n\ntest1: decorator')
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__) 
        return func(*args, **kw)
    return wrapper
f=log(now)
f()

now=log(now)
now()
print(f.__name__)
print(now.__name__)

#put @log here equal to now1=log(now1)
@log
def now1():
    print('now1')

# f
f=now1
f()
print(f.__name__)
print(now1.__name__)

print('\n\ntest2: decorator with args')
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#equal to now2=log2('excute')(now), log2() return decorator() function
@log2('excute')
def now2():
    print('now2')

now2()

print('\n\ntest3: decorator with args and functools')
import functools

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log3('log3 excute')
def now3():
    print('now3')

now3()

print('\n\ntest4: decorator with args and functools')
def log4(test=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if test != None:
                print('%s -- %s: ' % (test, func.__name__))
            else:
                print('call -- %s: ' % func.__name__)
            func(*args, **kw)
        return wrapper
    return decorator

@log4()
def now4():
    print('now4')
print()
now4()

print('\n\ntest5: decorator with args and functools')
@log4('excute')
def now5():
    print('now5')

now5()
