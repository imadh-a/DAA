class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def avl_insert(self, key):
        self.root = self._avl_insert(self.root, key)

    def _avl_insert(self, node, key):
        if node is None:
            return AVLTreeNode(key)

        if key < node.key:
            node.left = self._avl_insert(node.left, key)
        else:
            node.right = self._avl_insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def avl_search(self, key):
        return self._avl_search(self.root, key)

    def _avl_search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._avl_search(node.left, key)
        return self._avl_search(node.right, key)

    def avl_delete(self, key):
        self.root = self._avl_delete(self.root, key)

    def _avl_delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._avl_delete(node.left, key)
        elif key > node.key:
            node.right = self._avl_delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._avl_find_min(node.right)
                node.key = successor.key
                node.right = self._avl_delete(node.right, successor.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _avl_find_min(self, node):
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
avlt = AVLTree()
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for key in keys:
    avlt.avl_insert(key)

print("Inorder traversal:")
avlt.inorder_traversal(avlt.root)
print()

# Search test
assert avlt.avl_search(6).key == 6
assert avlt.avl_search(12) is None

# Delete test
avlt.avl_delete(6)
print("Inorder traversal after deleting 6:")
avlt.inorder_traversal(avlt.root)
print()
assert avlt.avl_search(6) is None
