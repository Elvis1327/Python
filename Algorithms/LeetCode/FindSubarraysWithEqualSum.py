

# Solution 1
def findSubarrays(nums = [4,2,4]):
    hash = {}
    res = 0
    for i in range(1,len(nums)):
        res = nums[i-1] + nums[i]
        if res not in hash:
            hash[res] = 0
        hash[res] += 1
    for j,k in hash.items():
        if k > 1:
            return True
    return False

# ******************
# Solution 2 with less code
def findSubarraysTwo(nums = [4,2,4]):
    hash = {}
    res = 0
    for i in range(1,len(nums)):
        res = nums[i-1] + nums[i]
        hash[res] = hash.get(res,0) + 1
    for j, k in hash.items():
        if k > 1:
            return True
    return False

# **************
# Another Approach
def findSubarraysThree(nums = [4,2,4]):
    hash = {}
    for i in range(len(nums) - 1):
        x = sum(nums[i:i+2])
        if x in hash:
            return True
        else:
            hash[x] = x
    return False

