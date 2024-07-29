
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 700. Search in a Binary Search Tree
# DFS APPROACH o(log(N))
def searchBST(root = [4,2,7,1,3], val = 2):
    # DFS In order Traversal
    # BIT O(LOG(N))
    def dfs(root):
        if not root:
            return None   
        if val < root.val:
            return dfs(root.left)
        elif val > root.val:
            return dfs(root.right)
        else:
            return root
    return dfs(root)
   
# DFS O(N)
# DFS In order Traversal
def searchBST(root = [4,2,7,1,3], val = 2):
    def dfs(root):
        if not root:
            return None   
        if root.val == val:
            return root
        return (dfs(root.left) or
        dfs(root.right))
    return dfs(root)





# BFS APROACH O(N)
def searchBST(root = [4,2,7,1,3], val = 2):
    if not root:
        return None
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val == val:
            return node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return None

