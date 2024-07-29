


def exist(self, 
          board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
          word = 'ABCCED'
          ):
    rows = len(board)
    cols = len(board[0])
    charS = set()
    
    def dfs(i, r, c):
        
        if i >= len(word):
            return True
        if (
            r < 0 or c < 0 or
            r >= rows or c >= cols or
            (r, c) in charS or
            board[r][c] != word[i]):
            return False
    
        charS.add((r, c))
        res = (
            dfs(i + 1, r + 1, c) or
            dfs(i + 1, r - 1, c) or
            dfs(i + 1, r, c + 1) or
            dfs(i + 1, r, c - 1)
        )
        charS.remove((r, c))
        return res
    
    for row in range(rows):
        for col in range(cols):
            if dfs(0, row, col):
                return True
    return False


# another approach
def exist2(self, 
          board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
          word = 'ABCCED'
          ):
    row = len(board)
    col = len(board[0])
    noRepeated = set()
    def backtracking(rows, cols, idx):
        if idx >= len(word):
            return True
        
        if (
            rows < 0 or cols < 0 or
            rows >= len(board) or cols >= len(board[0])
            or board[rows][cols] != word[idx] or
            (rows, cols) in noRepeated):
            return False
        
        noRepeated.add((rows, cols))
        if backtracking(rows + 1, cols, idx + 1):
            return True
        if backtracking(rows -1 , cols, idx + 1):
            return True
        if backtracking(rows, cols + 1, idx + 1):
            return True
        if backtracking(rows, cols - 1, idx + 1):
            return True
        noRepeated.remove((rows, cols))