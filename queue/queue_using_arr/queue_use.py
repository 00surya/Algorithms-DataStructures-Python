from queue import QueueUsingArray

q = QueueUsingArray()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while not q.isEmpty():
    print(q.front())
    q.dequeue()

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

