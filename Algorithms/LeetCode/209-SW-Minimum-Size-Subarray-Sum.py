

# Remember this is a Sliding Window Approach so we need to track 
# The indice of the window so we do left and right pointer for this problem
# We need another variabble to track the sum and if we do this at the beggining
# Then the while loop the second because when we hit the last element in the array
# We need to compare if currentSum is greater than target.

# SLIDING WINDOW ALGORITHM
def minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]):
    minSub = float('inf')
    left = 0
    currentSum = 0
    for right in range(len(nums)):
        currentSum += nums[right]
        while currentSum >= target:
            minSub = min(minSub, right - left + 1)
            currentSum -= nums[left]
            left += 1
    if minSub != float('inf'):
        return minSub
    return 0


