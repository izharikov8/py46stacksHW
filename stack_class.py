class Stack:
    def __init__(self):
        self.own_stack = []

    def isEmpty(self):
        if self.own_stack:
            return True
        else:
            return False

    def push(self, el):
        if self.own_stack:
            self.own_stack.insert(0, el)
        else:
            self.own_stack.append(el)

    def pop(self):
        if self.own_stack:
            self.own_stack.pop(0)
            return self.own_stack[0]
        else:
            return 'Stack is empty!'

    def peek(self):
        if self.own_stack:
            return self.own_stack[0]
        else:
            return 'Stack is empty!'

    def size(self):
        if self.own_stack:
            return len(self.own_stack)

#class methods
my_stack = Stack()
my_stack.own_stack = ['(', '(', '(', '(', '(', '[', '{', '}', ']', ')', ')', ')', ')', ')']
print(my_stack.own_stack)
print(my_stack.isEmpty())
my_stack.push('x')
print(my_stack.own_stack)
print(my_stack.pop())
print(my_stack.own_stack)
print(my_stack.peek())
print(my_stack.size())