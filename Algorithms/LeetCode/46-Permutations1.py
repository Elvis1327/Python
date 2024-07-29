

# PERMUTATIONS 1

#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Remember that a permutation is the number of ways that we can rearrenge one Object or Array
# Permutations of [1,2,3] -> [1,3,2], [2,3,1], [2,1,3] and so on....


def permute(self, nums = [1,2,3]):
    permutations = []
    res = []
    # Create two variables: Permutations and Response
    def dfs(i, permutations):
        # This is the base case of our Backtracking Algorithm so we backtrack 
        # if the length of permutations is equal to length of nums then we backtracking 
        if len(permutations) >= len(nums):
            res.append(permutations[:])
            return
        
        for idx in range(len(nums)):
        # We start a loop to evaluate or to start build candidates to our function
        # and if we find a solution with one option we return true else we BACKTRACK
        # and check for other options
            if nums[idx] not in permutations:
            # We compare if the number currentNum is in permutations we skip that number
                permutations.append(nums[idx])
                # Start looking for another option
                dfs(i + 1, permutations)
                # Pop a Number after backtracking
                permutations.pop()
    dfs(0, permutations)
    return res

