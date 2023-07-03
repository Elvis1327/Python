
# My Solution
def repeatedNTimes(nums = [1,2,3,3]):
    hash = {}
    for i in nums:
        hash[i] = hash.get(i,0) + 1
        if hash[i] > 1:
            return i

# Another Approach
def repeatedNTimes(nums = [1,2,3,3]):
    test = len(nums) // 2
    for i in nums:
        if nums.count(i) == test:
            return i



