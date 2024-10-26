RED = True
BLACK = False


class RedBlackTreeNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None

    def rb_insert(self, key):
        self.root = self._rb_insert(self.root, key)
        self.root.color = BLACK  # Ensure root is black

    def _rb_insert(self, node, key):
        if node is None:
            return RedBlackTreeNode(key)

        if key < node.key:
            node.left = self._rb_insert(node.left, key)
        elif key > node.key:
            node.right = self._rb_insert(node.right, key)

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def _is_red(self, node):
        return node is not None and node.color == RED

    def rb_search(self, key):
        return self._rb_search(self.root, key)

    def _rb_search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._rb_search(node.left, key)
        return self._rb_search(node.right, key)

    def rb_delete(self, key):
        self.root = self._rb_delete(self.root, key)
        if self.root:
            self.root.color = BLACK

    def _rb_delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._rb_delete(node.left, key)
        elif key > node.key:
            node.right = self._rb_delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._rb_find_min(node.right)
                node.key = successor.key
                node.right = self._rb_delete(node.right, successor.key)

        if node is None:
            return node

        node.color = BLACK
        return node

    def _rb_find_min(self, node):
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
rbt = RedBlackTree()
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for key in keys:
    rbt.rb_insert(key)

print("Inorder traversal:")
rbt.inorder_traversal(rbt.root)
print()

# Search test
assert rbt.rb_search(6).key == 6
assert rbt.rb_search(12) is None

# Delete test
rbt.rb_delete(6)
print("Inorder traversal after deleting 6:")
rbt.inorder_traversal(rbt.root)
print()
assert rbt.rb_search(6) is None
