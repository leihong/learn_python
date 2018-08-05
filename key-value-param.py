#!/usr/bin/env python3
#call function with keyworld param, must use key='value' for the keyworld param
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

print('person:')
person("Jack", 20, city='beijing')

mymap={'city':'beijing', 'job':'Engineer'}
person("Lucy", 20, **mymap)
person("Lucy", 20, city=mymap['city'], job=mymap['job'])
person("Lucy", 20, kk='kk')

#call function with named keyworld param, must use key='value' for the keyworld param, and must fill all the specified keyworld in the function 
def person1(name, age, *, city, job):
    print('name: ', name, 'age: ', age, 'city: ', city, 'job: ', job )

print('person1:')
mymap={'city':'beijing', 'job':'Engineer'}
#person1("Lucy", 20) #error
#person1("Lucy", 20, kk='kk') #error
#person1("Jack", 20, city='beijing') #error, need both city and job
person1("Jack", 20, city='beijing', job='Painter') 
person1("Jack", 20, **mymap) 

print('person2:')
def person2(name, age, *arg, city, job):
    print('name: ', name, 'age: ', age, 'city: ', city, 'job: ', job )


person2("Jack", 20, 'aa', city='beijing', job='Painter') 
person2("Jack", 20, 'bb', city='beijing', job='Painter') 

