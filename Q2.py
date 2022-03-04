# In a binary tree, implement a Python function count, that takes in an integer N
# and returns the number of times N appears in the binary tree.
# Note that this is not a binary search tree. What is the time complexity of your function?

class BinaryTree:
    class _Node:
        def __init__(self, element, left=None, right=None):
            self._left = left
            self._right = right
            self._element = element

        def __init__(self):
            self._root = None
            self._size = 0

        def count(self, N):
            if self.root is None:
                return 0
            queue = []
            queue.append(self.root)
            count = 0
            while (len(queue) > 0):
                node = queue.pop(0)
                if node._element == N:
                    count = count + 1
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            return count