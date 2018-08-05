#!/usr/bin/env python3

def variable_use(*a):
    t=0
    for i in a:
        t += i
    print(t)

variable_use(1,2,3,4)
mylist=[1,2,3]
variable_use(mylist[0],mylist[1], mylist[2])
variable_use(*mylist) # *mylist will expose it to mylist[0],mylist[1], mylist[2]

