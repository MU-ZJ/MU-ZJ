from collections import deque

stack = deque()

def push(x):
    stack.append(x)

def pop():
    stack.pop()

push("1")
push("2")
push("3")

print(stack)

pop()
pop()

print(stack)