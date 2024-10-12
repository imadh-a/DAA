class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size  # Fixed-size array
        self.top_index = -1  # Top of the stack is initially -1 (empty)

    def push(self, x):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.top_index += 1
        self.stack[self.top_index] = x

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        val = self.stack[self.top_index]
        self.top_index -= 1
        return val

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.size - 1

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top_index]

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack:", self.stack[:self.top_index + 1])


# Example usage
if __name__ == "__main__":
    stack = Stack(5)  # Create a stack of size 5
    print("Initial stack:")
    stack.print_stack()  # Stack is empty

    print("\nPushing elements onto the stack:")
    stack.push(100)
    stack.push(150)
    stack.push(250)
    stack.print_stack()

    print("\nTop element:", stack.top())

    print("\nPopping an element from the stack:")
    popped = stack.pop()
    print(f"Popped element: {popped}")
    stack.print_stack()

    print("\nIs the stack empty?", stack.is_empty())
    print("Is the stack full?", stack.is_full())

