
# Intuiton Solution
def twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]):
    # Create a result variable
    res = []
    # Iterate through first Array
    for i in nums1:
        # Compare if the numbers in the first Array are equal in the second Array and thrid Array
        # if are equal append to the res variable
        if i in nums2 or i in nums3:
            res.append(i)
            # Iterate through the second Array
    for j in nums2:
        # Compare if the numbers of the second Array are equal to the third Array, if yes append to the Variable
        if j in nums3:
            res.append(j)
    return set(res)

# **************************
# Another Approach
def twoOutOfThree2(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]):
    hash = {}
    res = []
    for i in set(nums1):
        hash[i] = hash.get(i,0) + 1
    for j in set(nums2):
        hash[j] = hash.get(j,0) + 1
    for k in set(nums3):
        hash[k] = hash.get(k,0) + 1
    for t in hash:
        if hash[t] > 1:
            res.append(t)




twoOutOfThree2()
