from sys import stdin
import queue

def reverseKElements(inputQueue, k):
    #Your code goes here
    # Approach queue1 to queue2 then k elements from queue2 to stack 
    # then stack to q1 and finally all the elements from q2 to q1
    s = []
    q = queue.Queue()
    while not inputQueue.isEmpty():
        q.put(inputQueue.get())
    for i in range(k):
        s.append(q.get())
    while len(s)>0:
    	inputQueue.put(s.pop())
    while q.isEmpty():
        inputQueue.put(q.get())

l = [1,23]
while len(l)>0:
    print(l.pop())