

# TRIVIAL PROBLEM
def palindromePartition(s = "aab"):
    # Backtracking Problem

    # Define first Variables
    res = []
    charS = []
    # Define a isPalindrome Function
    def isPal(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    # Define Backtracking Function 
    def backtracking(i, charS):
        # Recursive Case
        if i >= len(s):
            res.append(charS.copy())
            return
        # Base case
        for idx in range(i, len(s)): 
            if isPal(s, i, idx ):
                charS.append(s[i: idx + 1])
                backtracking(idx + 1, charS)
                charS.pop()
        
    backtracking(0, charS)
    return res
