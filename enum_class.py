#!/usr/bin/env python3

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1=Weekday.Mon
print('day1:', day1)
print('Weekday.Tue', Weekday.Tue)
print('Weekday\[\'Tue\'\]',Weekday['Tue'])
print('Weekday.Tue.value', Weekday.Tue.value)
print(Weekday.Mon == day1)
print(Weekday(1))
print('List all Weekday:')
for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',',  member.value)
