class MyStack:

    # initializes the stack object
    def __init__(self):
        self.stack = []

    # pushes the given value at the top of the stack
    def push(self, value):
        self.stack.append(value)

    # pops the top-most element from the stack
    def pop(self):
        if self.stack:
            self.stack.pop()
        return None

    # checks if the stack is empty or not
    def is_empty(self):
       return not self.stack

    # returns the top-most elenent of the stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    # returns the size of the stack
    def size(self):
        if self.stack:
            return len(self.stack)
        return None
        
        
if __name__ == '__main__':
    stack1 = MyStack()
    print(stack1.is_empty())
    print(stack1.push(1))
    print(stack1.stack)
    print(stack1.push(2))
    print(stack1.push(3))
    print(stack1.push(4))
    print(stack1.stack)
    print(stack1.pop())
    print(stack1.stack)
        
            
