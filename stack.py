class Stack:
    def __init__(self,n):
        self.stack = []
        self.n = n

    def push(self,k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The stack is full")

    def pop(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            self.stack.pop(-1)

    def top(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            return self.stack(-1)

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

plate = Stack(5)
plate.push(4)
plate.push(6)
plate.push(19)
plate.pop()
plate.display()
plate.push(7)
plate.push(10)
plate.push(19)
plate.display()
plate.push(12)
plate.display()