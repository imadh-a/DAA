class MinHeap:
    def __init__(self):
        self.heap = []

    def parent_node(self, i):
        return (i - 1) >> 1

    def left_node(self, i):
        return (i << 1) + 1

    def right_node(self, i):
        return (i << 1) + 2

    # Now we build a min heap from the given array.

    def build_min_heap(self, arr):

        self.heap = arr
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

    # We define a fucntion to Heapify the subtree whose root is index i.

    def min_heapify(self, i):

        l = self.left_node(i)
        r = self.right_node(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    # The next function returns the minimum element in the heap.

    def get_minimum(self):

        if not self.heap:
            return None
        return self.heap[0]

    # We here define a function that removes and returns the minimum element from the heap.

    def pop_minimum(self):

        if not self.heap:
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.min_heapify(0)
        return min_val

    # This fuction Inserts a new element into the heap while maintaining the heap property.

    def insert_value(self, val):

        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent_node(i)] > self.heap[i]:
            self.heap[self.parent_node(i)], self.heap[i] = self.heap[i], self.heap[self.parent_node(i)]
            i = self.parent_node(i)


# Lets implement an example for all the functions we have included.

heap = MinHeap()
heap.build_min_heap([24, 32, 8, 2, 3.1, 12, 18, 17.1])
print("Min Heap is:", heap.heap)

# insertion of an element into the heap
heap.insert_value(11)
print("After Inserting 9 :", heap.heap)

# printing the minimum value
print("Minimum Value (Root):", heap.get_minimum())

# popping the least value
print("Popped Minimum value (Root):", heap.pop_minimum())

# print back the updated heap
print("Heap after Popping the minimum value:", heap.heap)


# Define a custom data structure
class CustomDS:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


# First we create a min heap with custom data structures
heap = MinHeap()
heap.build_min_heap([CustomDS(18), CustomDS(6), CustomDS(14)])
print("Min Heap for custom Data Structure:")
for item in heap.heap:
    print(item.value, end=" ")

# Lets insert a new custom data structure into the heap
heap.insert_value(CustomDS(2.2))
print("\nAfter Inserting 2:")
for item in heap.heap:
    print(item.value, end=" ")

# Get the minimum value in the heap
print("\nMinimum Value:", heap.get_minimum().value)

# Pop the minimum value from the heap
print("Popped Minimum value:", heap.pop_minimum().value)

# Display the updated heap
print("Heap after Popping the minimum value:")
for item in heap.heap:
    print(item.value, end=" ")

