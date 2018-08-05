#!/usr/bin/env python3

#note for the default parameter, you should alway assign it an invarable value
def wrong_use(L=[]):
    L.append("END")
    return L

Test=wrong_use()
print(Test)
Test=wrong_use()
print(Test)
Test=wrong_use()
print(Test)

def correct_use(L=None):
    if L==None:
        L=[]
    L.append("End")
    return L

corr=correct_use()
print(corr)
corr=correct_use()
print(corr)
corr=correct_use([2])
print(corr)
