

# Missing Number Problem
# In this approach we can use a HashTale and then we iterate for each value in nums but we sum 1 value more becase 
# we need to find the number that is missing but is between len(nums)
# so we compute all the values of nums as a key in the HashTable and then compute the values in the HashTable
# and finally we compare if hash[i] not in nums, (if the number that is in hash[i] is not in nums we return that number)
def missingNumber(nums = [3,0,1]):
        hash = {}
        for i in range(len(nums) + 1):
            if i not in hash:
                hash[i] = i
            if hash[i] not in nums:
                 return hash[i]
missingNumber()

# ******************
# Less Code
def missingNumberLessCode(nums = [3,0,1]):
        hash = {}
        for i in range(len(nums) + 1):
            hash[i] = i
            if hash[i] not in nums:
                 return hash[i]
missingNumberLessCode()