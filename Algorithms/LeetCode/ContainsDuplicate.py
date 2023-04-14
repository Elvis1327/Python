# FIND DUPLICATE FIRST APPROACH

# BRUTE FORCE SOLUTION
def findDuplicateBruteForce(nums=[1,2,3,4,2]):
    for i in range(len(nums) -1):
        for j in range(i +1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Explanation: Use two for loops to compare pairs of integers in the array. 
# Once we reach a comparison in which the numbers are the same, we return true. 
# If we loop through all the integers of the array without reaching a similar pair of numbers, \
# we return false.
# Runtime: Time Limit Exceeded

# The problem with this Approach is that the time is Exceeded so if we have a List with
# 1000 numbers is linear so the time is a long time.

# *************************************

# SECOND APPROACH FIRST METHOD USING SET
def findDuplicateSetFirst(nums=[1,2,3,4,2]):
    x = set(nums)
    if len(x) == len(nums):
        return False
    return True

# FIND DUPLICATE SECOND METHOD USING SET
def findDuplicateSetSecond(nums=[1,2,3,4,2]):
    x = set()
    for i in nums:
        if i in x:
            return True
        x.add(i)
    return False

# ***************************

# TRIRD APPROACH WITH HASHTABLE FIRST METHOD
def findDuplicateHashTableFirst(nums=[1,2,3,4,2]):
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 0
        else:
            return True
    return False

# FIND DUPLICATE WITH HASHTABLE SECOD METHOD
def findDuplicateHashTableSecondMethod(nums=[1,2,3,4,2]):
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 0
        hash[i] += 1
    for j, freq in hash.items():
        if freq > 1:
            return True
    return False
findDuplicateHashTableSecondMethod()

# LAST WAY HASH TALBE
def findDuplicateHashTableThrirdMethod(nums=[1,2,3,4,2]):
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 0
        hash[i] = hash.get(i, 0) + 1
    print(hash)
    for j, freq in hash.items():
        if freq > 1:
            return True
    return False
findDuplicateHashTableSecondMethod()
    