from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)

#除了从普通元组那里继承来的属性外，具名元组还有一些自己专有的属性。
#常用的有： _fields类属性 , _make(iterable)类方法,_asdict()实例方法
print('City._fields:', City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.93, LatLong(28.613889, 77.2))
delhi = City._make(delhi_data);
print(delhi._asdict())
print(delhi)
print(tokyo)

for key, value in delhi._asdict().items():
    print(key+':', value)