

def letterCombinations(digits = "23") :
    res = []
    charS = []
    # My problem with this problem was to notice how to iterate the data structure
    if len(digits) == 0:
        return []
    # Create a hashTable for the telephone
    # We are going to iterate over this hashTable 
    tel = {
        "2": 'abc',
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    # Start our backtracking Algorithm
    def backtracking(i):
        # Recursive case, if the indice is greater or equal to length digits we append the value
        # then we backtrack remember this is just a combination problems
        if i >= len(digits):
            res.append("".join(charS))
            return
        
        # Loop for the combinations
        for digit in tel[digits[i]]:
            charS.append(digit)
            backtracking(i + 1)
            charS.pop()
        
    backtracking(0)
    return res
        
    backtracking(0)