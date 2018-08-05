#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        #if not isinstance(val, int):
        #    raise ValueError('score must be an interger!')
        #if val<0 or val>100:
        #    raise ValueError('score must be in the range[0,100]')
        self._score = val

a = Student()
#print(a.score)
a.score = 100
print(a.score)
