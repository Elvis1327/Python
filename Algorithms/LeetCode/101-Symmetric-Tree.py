

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# O(N)
def isSymmetric( root = [1,2,2,3,4,4,3] ):
    # DFS ALGORITHM
    def dfs(left, right):
        if not left and not right:
            return True
       
        if left and not right:
            return False
        
        if right and not left:
            return False
        
        if left.val != right.val:
            return False
        
        return (
            dfs(left.left, right.right ) and dfs(left.right, right.left)
        )
    return dfs(root.left, root.right)

