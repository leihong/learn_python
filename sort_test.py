
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

print(fruits)

print(fruits.sort())
print(fruits)


import bisect
import sys
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))

bisect_fn = bisect.bisect_left #bisect_left = bisect
print('DEMO bisect_left:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

bisect_fn = bisect.bisect_right
print('\n\nDEMO bisect_right:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)


print('\n\nbitsect.insort sample(insert sort):')
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)

    #insort = insort_left
    #there have another function insort_right
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

