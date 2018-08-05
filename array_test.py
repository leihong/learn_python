from array import array
from  random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)

floats2 = array('d')
with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10**7)

print(floats2[-1])
print(floats2 == floats)

from collections import deque
import queue

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.append(-1)
print(dq)

dq.extend([11,22,33])
print(dq)

dq.extendleft([10,20,30,40])
print(dq)

q = queue.Queue(10)
l=[q.put(i) for i in range(10)]
print(l)
while not q.empty():
    print(q.get(), end=' ')
print('')

lifoQ = queue.LifoQueue(10)
[lifoQ.put(i*i) for i in range(5)]
print('lifoQ maxsize:', lifoQ.maxsize)
print('lifoQ full:', lifoQ.full())
print('lifoQ empty:', lifoQ.empty())
print('lifoQ qsize:', lifoQ.qsize())

while not lifoQ.empty():
    print(lifoQ.get(), end=' ')
print('\n\n')

import multiprocessing
import threading
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('Job:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

pQ = queue.PriorityQueue()
pQ.put(Job(3, 'level 3 job'))
pQ.put(Job(10, 'level 10 job'))
pQ.put(Job(1, 'level 1 job'))

def process_job(q):
    while True:
        next_job = q.get()
        print('for:', next_job.description)
        q.task_done()

workers = [threading.Thread(target=process_job, args=(pQ,)),
           threading.Thread(target=process_job, args=(pQ,))]

for w in workers:
    w.setDaemon(True)
    w.start()

pQ.join()

# multiprocessing.Queue
