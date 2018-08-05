#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    class_count=0
    def __init__(self, obj_count, name):
        self.name = name
        self.obj_count = obj_count
        Student.class_count +=1
        self.__private = "This is an private parameter of " + name
    def get_private(self):
        return self.__private

s1 = Student(1, 'Amy')
s2 = Student(3, 'Andy')
s3 = Student(2, 'Jack')

print(s1.class_count)
print(s2.class_count)
print(s3.class_count)

print(s1.obj_count)
print(s2.obj_count)
print(s3.obj_count)

print(s1.name)
print(s2.name)
print(s3.name)

print(s1.get_private())
print(s2.get_private())
print(s3.get_private())


#private parameters can not be called directly, need define a function 
#print(s1.__private)
#print(s2.__private)
#print(s3.__private)

#the private parameter have been renamed to _Student__nane
#but don't call like this, it maybe different of every python parser
#print(s1._Student__name)
s1.__private = 'this is an new __private different to the private parameter'
print(s1.__private)
print(s1.get_private())
print(s1.__private)
