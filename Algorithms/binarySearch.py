
# Iterative way
def binarySearch(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        potentionalMath = arr[m]
        if potentionalMath == target:
            return m
        elif target < potentionalMath:
            r = m - 1
        else:
            l = m + 1 
    return -1
    
print(binarySearch([3,6,9,14,17,40,72], 9))

# //////////////////////////////////

# Recursive
def binarySearchRecursive(nums, target):
    return helper(nums, target, 0, len(nums) - 1)

def helper(nums, target, left, right):

    if left > right:
        return -1 
    m = (left + right) // 2
    res = nums[m]
    if target == res:
        return m
    elif target < res:
        return helper(nums, target, left, m - 1)
    else:
        return helper(nums, target, m + 1, right)

print(binarySearchRecursive([5,8,10,14,23,50,70], 23))