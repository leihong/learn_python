#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Student0(object):
    pass

s = Student0()
s.name = 'Michael'
s.age = 25
s.score = 99
print("name=%s, age=%d, score=%d" % (s.name, s.age, s.score))
class Student(object):
    #tell the Student class only have 2 varible for use: 'name' and 'age'
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
#error: Student only have two varible: name and age
s.core = 99
