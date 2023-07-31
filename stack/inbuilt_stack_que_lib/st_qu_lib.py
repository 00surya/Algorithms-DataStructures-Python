# import queue

# #inbuilt stack
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)

# while not q.empty():
#     print(q.get(), end=" ")
# print()
# # order will be 3,2,1

# #inbulit queue
# q = queue.Queue()

# q.put(1)
# q.put(2)
# q.put(3)

# print(q.qsize())
# # print(q.front())

# # while not q.empty():
# #     print(q.get(),end=" ")

# # order will be 1,2,


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Dequeue:
    
#     def __init__(self):
#         self.head = None
        
#     def insertFront(self,data):
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#             return
#         next_to_head = self.head.next
#         self.head = node
#         self.head.next = next_to_head
    
#     def insertRear(self,data):
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = node

#     def deleteFront(self):
#         if self.head == None:
#             return -1
#         front_elem = self.head
#         self.head = self.head.next
#         return front_elem.data
    
    
#     def deleteRear(self):
#         if self.head == None:
#             return -1
        
#         if(self.head.next == None):
#             last_node = self.head
#             self.head = None
#             self.tail = None
#             return last_node.data
#         else:
#             temp = self.head
#             while(temp.next.next != None):
#                 temp = temp.next
#             last_node = temp.next
#             temp.next = None
#             return last_node.data

        

    
#     def getFront(self):
#         if self.head:
#             return self.head.data
#         return -1
    
#     def getRear(self):
#         if self.head == None:
#             return -1
#         if self.head.next == None:
#             print("hello")
#             return self.head.data
#         else:
#             temp = self.head
#             while(temp.next.next != None):
#                 temp = temp.next
#             return temp.next.data
    

class Dequeue:
    def __init__(self, size):
        self.dq = [0 for i in range(size)]
        self.n = size
        self.front = -1
        self.rear = -1

    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def insertFront(self, x):
        if(self.isFull() == True):
            # Deque is full.
            return False
        if(self.isEmpty() == True):
            # Deque is empty.
            self.front = self.rear = 0
        else:
            # Deque is NOT empty. So, decrement 'front' by 1.
            if (self.front == 0):
                self.front = self.n-1
            else:
                self.front -= 1

        # Insert the element at the front of deque.
        self.dq[self.front] = x
        return True

    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def insertRear(self, x):
        if(self.isFull() == True):
            # Deque is full.
            return False
        if(self.isEmpty() == True):
            # Deque is empty.
            self.front = self.rear = 0
        else:
            # Deque is NOT empty. So, increment 'rear' by 1.
            if (self.rear == self.n-1):
                self.rear = 0
            else:
                self.rear += 1

        # Insert the element at the end of deque.
        self.dq[self.rear] = x
        return True

    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def deleteFront(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1

        item = self.dq[self.front]

        if(self.front == self.rear):
            # Deque has only one element.
            self.front = self.rear = -1
        else:
            # Increment 'front' by 1.
            if (self.front == self.n-1):
                self.front = 0
            else:
                self.front += 1

        return item

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def deleteRear(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1

        item = self.dq[self.rear]

        if(self.front == self.rear):
            # Deque has only one element.
            self.front = self.rear = -1
        else:
            # Decrement 'rear' by 1.
            if (self.rear == 0):
                self.rear = self.n-1
            else:
                self.rear -= 1

        return item

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1
        return self.dq[self.front]

    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        if(self.isEmpty() == True):
            # Deque is empty.
            return -1
        return self.dq[self.rear]
        
    def isEmpty(self):
        if(self.front == -1):
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        if ((self.front == 0 and self.rear == self.n - 1) or (self.front == self.rear + 1)):
            return True
        return False
#main
from sys import stdin
inputs = stdin.readline().strip().split(" ")
s = inputs.__len__()
queue = Dequeue(s)
i = 0
ans = []
while i < len(inputs)-1:
    choice = inputs[i]
    if choice == '1':
        data = inputs[i+1]
        queue.insertFront(data)
        i += 2
    elif choice == '2':
        data = inputs[i+1]
        queue.insertRear(data)
        i += 2

    elif choice == '3' :
        queue.deleteFront()
        i+=1

    elif choice == '4' : 
        print(queue.deleteRear())
        i+=1
    elif choice == '5':
        print(queue.getFront())
        i+=1
    else:
        print(queue.getRear())
        i+=1


# print(inputs)


