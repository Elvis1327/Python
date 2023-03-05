

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)

#       1
#      /\
#     2  3
#    /\   \ 
#   4  5   6 

# Recursive Way
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


print(inorderTraversal(n1))



