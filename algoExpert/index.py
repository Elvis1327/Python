class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

        #       1
        #      / \
        #     2   3
        #    /     \
        #   4      5

# def DFS(vector):
#     values = []
#     def helper(vector):
#         if vector == None:
#             return values
#         helper(vector.left)
#         values.append(vector.value)
#         helper(vector.right)
#     helper(vector)
#     print(values)
#     return values

# DFS(root)

def dfsStack(vector):
    stack = []
    while stack == []:
        curr = stack.pop()
        if curr.left != None:
            stack.append(curr.left)
        if curr.right != None:
            stack.append(curr.right)
    print(stack)

dfsStack(root)


