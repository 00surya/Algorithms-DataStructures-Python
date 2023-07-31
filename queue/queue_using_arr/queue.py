class QueueUsingArray:

    def __init__(self):
        self.__arr= []
        self.__count = 0
        self.__front = 0
    
    def enqueue(self,data):
        self.__arr.append(data)
        self.__count += 1
    
    def dequeue(self):
        if self.__count == 0:
            return -1
        elem = self.__arr[self.__front]
        self.__front += 1
        self.__count -= 1
        return elem

    def front(self):
        if self.__count == 0:
            return -1
        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

