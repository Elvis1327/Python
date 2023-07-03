
# My Solution
def findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]):
    res = []
    hash = {}
    nums_set = set(nums)
    for i in range(1,len(nums) + 1):
        hash[i] = i
    for j, k in hash.items():
        if k not in nums_set:
            res.append(k)
    return res

# ***************
# Another Approach optimazed solution
def findDisappearedNumbersSecond(nums = [4,3,2,7,8,2,3,1]):
    res = []
    num_set = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in num_set:
            res.append(i)
    return res