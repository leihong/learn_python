#!/usr/bin/env python3

L=sorted([36,5,6,3,-8,55,-9])
print(L)


L=sorted([36,5,6,3,-8,55,-9], key=abs)
print(L)

L=sorted(['bob','about','Zoo','Credit card', 'Credit user', 'credit user'])
print(L)

L=sorted(['bob','about','Zoo','Credit card', 'Credit user', 'credit user'], key=str.lower)
print(L)

#reverse
L=sorted(['bob','about','Zoo','Credit card', 'Credit user', 'credit user'], key=str.lower, reverse=True)
print(L)

def by_name(T):
    return T[0].lower()

L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L=sorted(L1, key=by_name) 
print(L)

def by_score(T):
    return -T[1]
L=sorted(L1, key=by_score) 
print(L)
