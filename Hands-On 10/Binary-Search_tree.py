class BasicBinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BasicBinarySearchTree:
    def __init__(self):
        self.root = None

    def basic_insert(self, key):
        self.root = self._basic_insert(self.root, key)

    def _basic_insert(self, node, key):
        if node is None:
            return BasicBinaryTreeNode(key)
        if key < node.key:
            node.left = self._basic_insert(node.left, key)
        elif key > node.key:
            node.right = self._basic_insert(node.right, key)
        return node

    def basic_search(self, key):
        return self._basic_search(self.root, key)

    def _basic_search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._basic_search(node.left, key)
        return self._basic_search(node.right, key)

    def basic_delete(self, key):
        self.root = self._basic_delete(self.root, key)

    def _basic_delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._basic_delete(node.left, key)
        elif key > node.key:
            node.right = self._basic_delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._basic_find_min(node.right)
                node.key = successor.key
                node.right = self._basic_delete(node.right, successor.key)
        return node

    def _basic_find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

# Test
bbst = BasicBinarySearchTree()
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for key in keys:
    bbst.basic_insert(key)

print("Inorder traversal:")
bbst.inorder_traversal(bbst.root)
print()

# Search test
assert bbst.basic_search(6).key == 6
assert bbst.basic_search(12) is None

# Delete test
bbst.basic_delete(6)
print("Inorder traversal after deleting 6:")
bbst.inorder_traversal(bbst.root)
print()
assert bbst.basic_search(6) is None
