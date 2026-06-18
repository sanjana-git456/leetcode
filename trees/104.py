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

def maximum(node):
    if node is None:
        return 0
    left = maximum(node.left)
    right = maximum(node.right)
    return 1+max(left, right)
print(maximum(root))