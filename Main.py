import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
         return self.top<=-1

    def is_full(self):
         return (len(self.stack)-1)==self.top

    def push(self, data):
        if not self.is_full():
            self.top=self.top+1
            self.stack[self.top]=int(input('enter the data:'))
            print(self.stack)
         else:
            print("stack is full")

    def pop(self):
        if not self.is_empty():
            # Write code here

    def status(self):


# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()

