

def maximumCount(nums = [-2,-1,-1,1,2,3]):
    pos = 0
    neg = 0
    for i in nums:
        if i < 0:
            neg += 1
        if i > 0:
            pos += 1
    return max(neg,pos)


