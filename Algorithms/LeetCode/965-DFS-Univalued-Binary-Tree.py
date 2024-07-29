
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.


# O(N)
def isUnivalTree( root = [1,1,1,1,1, None ,1]):
    if not root:
        return None
    value = root.val
    def dfs(root):
        if not root:
            return None
        if root.val != value:
            return False
        if dfs(root.left)== False:
            return False
        if dfs(root.right) == False:
            return False
    if dfs(root) == False:
        return False
    return True

# Shorter Code O(N)
def isUnivalTree( root = [1,1,1,1,1, None ,1]):
    if not root:
        return None
    
    value = root.val
    def dfs(root):
        if not root:
            return True
        
        if root.val != value:
            return False
        
        return(
            dfs(root.left) and dfs(root.right)
        )
    return dfs(root)

