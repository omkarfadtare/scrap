# In a binary search tree:
# What is worst case time complexity of the binary search function?
# Provide an example binary search tree that exhibits worst case running time of binary_search function.
# Write a function that prints elements in binary search tree in order.

# Ans- # worst case time complexity of the binary_search function = O(n) n is number of elements in BST


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def insert_element(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_element(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_element(root.left, node)
def binary_search(root,key):
    print(root.val)
    if root is None or root.val == key:
        return root
        if root.val < key:
            return binary_search(root.right,key)
            return binary_search(root.left,key)
r = Node(10)
insert_element(r,Node(20))
insert_element(r,Node(30))
insert_element(r,Node(40))
insert_element(r,Node(50))
insert_element(r,Node(60))
insert_element(r,Node(80))
binary_search(r,80)