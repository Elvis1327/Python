
def test(nums = [3,0,1]):
    hash = {}
    for i in range(len(nums)):
        if i not in hash:
            hash[i] = nums[i]
    for j in hash:
        if j not in nums:
            print(j)

test()




