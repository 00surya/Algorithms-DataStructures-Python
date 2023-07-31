
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    #Define data members and __init__()
    def __init__(self):
        self.head = None
        self.count = 0


    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.count



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.count == 0



    def push(self, data) :
        #Implement the push(element) functi
        node = Node(data)
        if not self.head:
            self.head = node
            self.count += 1
            return
        next_to_head = self.head
        self.head = node
        self.head.next = next_to_head
        self.count += 1
        return    
	

    def pop(self) :
        #Implement the pop() function
        if self.isEmpty():
            # print("Hey! Stack is Empty!!")
            return -1
        
        last_head = self.head
        self.head = last_head.next
        self.count -= 1
        return last_head.data

    def top(self) :
        #Implement the top() function
        if not self.isEmpty():
	        return self.head.data
        return -1
        




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1

