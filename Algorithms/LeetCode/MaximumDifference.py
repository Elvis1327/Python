

# Looking for 
def maximumDifference( nums = [7,1,5,4] ):
    res = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            res.append(nums[j] - nums[i])
    if max(res) <= 0:
        return -1
    return max(res)


