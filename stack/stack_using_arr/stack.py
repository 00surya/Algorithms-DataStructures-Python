class Stack:

    def  __init__(self):
        self.__data = []

    def push(self,item):
        self.__data.append(item)


    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!!")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!")
            return
        return self.__data[::-1]


    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size()==0


