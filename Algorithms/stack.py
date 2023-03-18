class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
        return self.stack
    def pop(self, data):
        self.stack.pop(self.stack.index(data))
        return self.stack
    def isempty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[-1]
    
sol = Stack()
print(sol.push(5))
print(sol.push(6))
print(sol.isempty())
print(sol.peek())
print(sol.push(8))
print(sol.push(7))
print(sol.pop(7))
print(sol.pop(8))