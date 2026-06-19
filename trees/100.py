class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

def isSame(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    return isSame(node1.left,node2.left) and isSame(node1.right,node2.right)
print(isSame(root1,root2))