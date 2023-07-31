from stack import Stack

s = Stack()
s.push(1)
s.push(12)
s.push(13)
s.push(14)

while s.isEmpty() is False:
    print(s.pop())

s.top()
