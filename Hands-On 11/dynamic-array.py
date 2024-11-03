import ctypes

class Array:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = self._create_array(self.capacity)

    def __len__(self):
        return self.size

    def _create_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_data = self._create_array(new_capacity)
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def add(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def get(self, index):
        if not 0 <= index < self.size:
            raise IndexError('Index out of range')
        return self.data[index]

# Example usage:
array_example = Array()
array_example.add(10)
array_example.add(20)
array_example.add(30)

print("Length of the array:", len(array_example))
print("Elements of the array:", [array_example.get(i) for i in range(len(array_example))])

array_example.add(40)
print("Length after adding an element:", len(array_example))
print("Elements after adding an element:", [array_example.get(i) for i in range(len(array_example))])


