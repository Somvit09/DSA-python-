top = -1
n = int(input("enter arrey value "))
stack = []
for _ in range(n):
    stack.append(int(input("enter elements of stack ")))


def push(x, top):
    print(x, " is the entered value of the stack")
    if top == n - 1:
        print("overflowed")
    else:
        top += 1
        stack[top] = x


def pop(temp, top):
    if top == -1:
        print("underflowed")
    else:
        temp = stack[top]
        top -= 1
        print("removed item is ", temp)


def peek(top):
    if top == -1:
        print("stack is empty")
    else:
        print("topmost elem,ent is ", stack[top])


def display(stack):
    for i in stack[::-1]:
        print(i, end=" ")



display(stack)
