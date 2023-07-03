
# First Solution Intuition
def shuffleArray(nums = [2,5,1,3,4,7], n= 3):
    l = n
    res = []
    for i in range(len(nums)):
        res.append(nums[i])
        res.append(nums[l])
        l += 1
        if len(res) == len(nums):
            return res
        
# Second Solution reducing use of pointer
def shuffleArraySecond(nums = [2,5,1,3,4,7], n= 3):
    res = []
    for i in range(len(nums)):
        res.append(nums[i])
        res.append(nums[n])
        n += 1
        if len(res) == len(nums):
            return res

# ***************
#   This is the faster solution
def shuffleArrayThree(nums = [2,5,1,3,4,7], n = 3):
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

# ***************** Two pointers
def shuffleArrayFour(nums = [2,5,1,3,4,7], n = 3):
    l = 0
    r = n
    res = []
    while l < n:
        res.append(nums[l])
        res.append(nums[r])
        l += 1
        r += 1
    return res
