
# First Approach: this is my solution full intuition
# I created an empty array and two arrays more then append everything depending on the if statement
def findDifference(nums1 = [1,2,3], nums2 = [2,4,6]):
    res = []
    n1, n2 = [], []
    for i in nums1:
        if i not in nums2:
            n1.append(i)
    res.append(set(n1))
    for j in nums2:
        if j not in nums1:
            n2.append(j)
    res.append(set(n2))
    return res

# ****************
# Another Approach Second One
def findDifferenceSecond(nums1 = [1,2,3], nums2 = [2,4,6]):
    res=[[],[]]
    for i in range(len(nums1)):
        if nums1[i] not in nums2 and nums1[i] not in res[0]:
            res[0].append(nums1[i])
    for i in range(len(nums2)):
        if nums2[i] not in nums1 and nums2[i] not in res[1]:
            res[1].append(nums2[i])
    return res

# ***********************
# Third Approach
def findDifferenceThrird(nums1 = [1,2,3], nums2 = [2,4,6]):
    a, b = set(nums1), set(nums2)
    return [list(a - b), list(b - a)]



