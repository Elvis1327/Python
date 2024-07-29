       

    # ***********************
    # PATH SUM PROBLEM
    # **********************


class BinaryTreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

 # This is a DFS Algorithm with backtracking
def dfs(root, currentSum = 0, targetSum = 22):
    # We pass the currentSum like parameter because when we do backtracking the currentSum update if we decide
    if not root:
        return None
    
    # Comparting if the currentSum is equal to target sum
    currentSum += root.val
    if not root.left and not root.right and currentSum != targetSum:
        currentSum -= root.val
        return
    if not root.left and not root.right and currentSum == targetSum:
        return True
    if dfs(root.left, currentSum):
        return True
    
    if dfs(root.right, currentSum):
        return True
    
    return dfs(root, 0)



