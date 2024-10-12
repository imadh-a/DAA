class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def delete(self, x):
        if self.head is None:
            raise ValueError(f"Value {x} not found in list")

        # If the head is the node to be deleted
        if self.head.data == x:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != x:
            current = current.next

        if current.next is None:
            raise ValueError(f"Value {x} not found in list")

        # Delete the node
        current.next = current.next.next

    def search(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        return False

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            print("Linked list:", end=" ")
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")



if __name__ == "__main__":
    sll = SinglyLinkedList()
    print("Initial linked list:")
    sll.print_list()  # Linked list is empty

    print("\nInserting elements into the linked list:")
    sll.insert(100)
    sll.insert(150)
    sll.insert(250)
    sll.print_list()

    print("\nSearching for element 150:")
    print("Is 150 in the list?", sll.search(150))

    print("\nDeleting element 150:")
    sll.delete(150)
    sll.print_list()

    print("\nSearching for element 150:")
    print("Is 150 in the list?", sll.search(150))

