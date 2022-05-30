

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorderTraversal(root):
    res = []
    def dfs(root):
        if root == None:
            return res
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    dfs(root)
    return res    

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)

print(inorderTraversal(n1))



