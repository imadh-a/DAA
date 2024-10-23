class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class UniqueHashTable:
    def __init__(self, initial_capacity=10):
        self.table_size = initial_capacity
        self.num_items = 0
        self.load_threshold = 0.75  # Threshold for resizing
        self.buckets = [None] * self.table_size

    def compute_hash(self, key):
        # Multiplication hash function
        golden_ratio = 0.61803398875
        return int(self.table_size * ((key * golden_ratio) % 1))

    def insert_item(self, key, value):
        index = self.compute_hash(key)
        node = self.buckets[index]
        new_node = HashNode(key, value)

        if node is None:
            self.buckets[index] = new_node
        else:
            while node.next:
                node = node.next
            node.next = new_node
        self.num_items += 1

        # Resize if load factor exceeds threshold
        if self.num_items >= self.table_size * self.load_threshold:
            self.resize_table(self.table_size * 2)

    def remove_item(self, key):
        index = self.compute_hash(key)
        node = self.buckets[index]
        prev_node = None

        while node:
            if node.key == key:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.buckets[index] = node.next
                self.num_items -= 1
                return
            prev_node = node
            node = node.next

        # Resize if load factor drops below 1/4
        if self.num_items < self.table_size * 0.25 and self.table_size > 1:
            self.resize_table(self.table_size // 2)

    def retrieve_value(self, key):
        index = self.compute_hash(key)
        node = self.buckets[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize_table(self, new_capacity):
        old_buckets = self.buckets
        self.table_size = new_capacity
        self.num_items = 0
        self.buckets = [None] * self.table_size

        for bucket in old_buckets:
            while bucket:
                self.insert_item(bucket.key, bucket.value)
                bucket = bucket.next

    def __str__(self):
        result = ''
        for bucket in self.buckets:
            while bucket:
                result += f'({bucket.key}: {bucket.value}) -> '
                bucket = bucket.next
        return result + 'None'


# Example usage
hash_table = UniqueHashTable()
hash_table.insert_item(5, 10)
hash_table.insert_item(15, 20)
hash_table.insert_item(25, 30)
print(hash_table.retrieve_value(15))
hash_table.remove_item(15)
print(hash_table.retrieve_value(15))
