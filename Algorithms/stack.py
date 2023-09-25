class stack:
    def __init__(self):
        self.stack_ = []
    def push(self, data):
        self.stack_.append(data)

    def pop_(self):
        self.stack_.pop()
    def pop_with_value(self, data):
        self.stack_.pop(self.stack_.index(data))
    def isempty(self):
        return len(self.stack_) == 0
    def peek(self):
        return self.stack_[-1]
    def print_s(self):
        print(self.stack_[::-1])
    
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_s()
s.pop_()
s.print_s()
s.pop_with_value(1)
s.print_s()
print(s.isempty())
print(s.peek())
s.print_s()
# stack will be like this - [4, 3, 2, 1], pop will eliminate the top value which is also peek value
# peek - 4, if pop() function called 4 will be removed, pop_with_data() need index to delete the index based 
# value, atlast this operation the output will like this -
'''
[4, 3, 2, 1]
[3, 2, 1]
[3, 2]
False
3
[3, 2]
'''