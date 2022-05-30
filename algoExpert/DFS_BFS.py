class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

def dfsImplementation(root):
    res = []
    stack = []
    cur = root
    while cur != None or stack != []:
        while cur != None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.value)
        cur = cur.right 

    return res


    #              1
    #             /\
    #            2  3
    #           /\   \ 
    #          4  5   6 

# Recursive
# Still is bad solution
def dfsRecursive(root):
    res = []
    if root == None:
        return []

    dfsRecursive(root.left)
    res.append(root.value)
    dfsImplementation(root.right)
    return res

