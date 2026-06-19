class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def swap(node):
    if node is None:
        return
    node.left,node.right = node.right,node.left
    swap(node.left)
    swap(node.right)
    return node
swap(root)