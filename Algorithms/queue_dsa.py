# queue implementation by queue.Queue
from queue import Queue

# initializing queue
qs = Queue(maxsize=10)
#printing queue size
print(qs.qsize())
# appending 1 by FIFO method
qs.put(1)
# checking queue is empty or not
print(qs.empty())
# checking queue is full or not
print(qs.full())
# removing the element
print(qs.get())
# checking the size again
print(qs.qsize())



# queue implementation with list

queue = []
# adding element
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# printing element
print(queue)
# removing element
queue.pop(0)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)

# queue implementation with collections.dequeue

from collections import deque

q = deque()
# printing element
print(q)
# adding element
q.append(1)
q.append(2)
q.append(3)
q.append(4)
# printing element
print(q)
# removing element
q.popleft()
q.popleft()
q.popleft()
# printing element
print(q)




