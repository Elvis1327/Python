
# Brute Force SLIDING WINDOW FIZED SIZE
def slidingWindowBruteForce(nums = [1,2,3,2,3,3], k = 3):
    for i in range(len(nums)):
        for j in range(i + 1, min(len(nums), i + k)):
            print(nums[i], nums[j])
 
# SLIDING WINDOW FIZED SIZE
# (Problem) Given an Array return true if there are two elements
# within a window of size k that are equal
def slidingWindowFizedSize(nums = [1,2,3,2,3,3], k = 3):
    window = set()
    l = 0
    for i in range(len(nums)):
        if i - l + 1 > k:
            window.remove(nums[l])
            print(i)
            l += 1
        if nums[i] in window:
            return True
        window.add(nums[i])
slidingWindowFizedSize()


# SLIDING WINDOW VARIABLE SIZE Brute Force
def slidingWindowFizedVariableBruteForce(nums = [4,2,2,3,3,3]):
    total = 0
    left = 0
    for i in range(len(nums)):
        if nums[left] != nums[i]:
            left = i
        total = max(total, i - left + 1)
    return total
    
# **********************
# Dinamyc Sliding Window
def SlidingWindowDynamic(nums = [2,3,1,2,4,3]):
    test = float('inf')

    print(test)
    
SlidingWindowDynamic()

