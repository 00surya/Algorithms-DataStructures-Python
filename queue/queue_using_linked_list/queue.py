
from sys import stdin


#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        #Implement the getSize() function
        return self.__count


    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.__count == 0


    def enqueue(self, data) :
        #Implement the enqueue(element) function
        node = Node(data)
        if self.__head == None:
            self.__head = node
            self.__tail = self.__head
            self.__count += 1
            return

        self.__tail.next = node
        self.__tail = node
        self.__count += 1
        return

    def dequeue(self) :
        #Implement the dequeue() function
        if self.__count == 0:
            return -1
        elem = self.__head
        self.__head = self.__head.next
        self.__count -= 1
        return elem.data



    def front(self) :
        #Implement the front() function
        if self.__count > 0:
        	return self.__head.data    
        return -1