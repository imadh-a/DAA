class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front_index = 0
        self.rear_index = 0
        self.count = 0

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("Queue overflow")
        self.queue[self.rear_index] = x
        self.rear_index = (self.rear_index + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        val = self.queue[self.front_index]
        self.front_index = (self.front_index + 1) % self.size
        self.count -= 1
        return val

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front_index]

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", end=" ")
            for i in range(self.count):
                print(self.queue[(self.front_index + i) % self.size], end=" ")
            print()


# Example usage
if __name__ == "__main__":
    queue = Queue(5)
    print("Initial queue:")
    queue.print_queue()

    print("\nEnqueueing elements into the queue:")
    queue.enqueue(100)
    queue.enqueue(150)
    queue.enqueue(250)
    queue.print_queue()

    print("\nFront element:", queue.front())

    print("\nDequeuing an element from the queue:")
    dequeued = queue.dequeue()
    print(f"Dequeued element: {dequeued}")
    queue.print_queue()

    print("\nIs the queue empty?", queue.is_empty())
    print("Is the queue full?", queue.is_full())

