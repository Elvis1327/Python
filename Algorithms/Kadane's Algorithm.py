
# BRUTE FORCE APPROACH Kadane's Algorithm
def bruteForce(nums = [4,-1,2,-7,3,4]):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            print("Start")
            curSum += nums[j]
            print(curSum, "this happen first")
            maxSum = max(maxSum, curSum)
            print(maxSum, "This happen after")
        print('this is the final of the first loop')     
bruteForce()

# ******************************
# This is the Kadane's Algorithm
def kadaneAlgorithm(nums = [4,-1,2,-7,3,4]):
    maxSum = nums[0]
    currentSum = 0
    for n in nums:
        currentSum = max(currentSum, 0)
        currentSum += n
        maxSum = max(maxSum, currentSum)
kadaneAlgorithm()

# *******************
# This is the Sliding Window Variation
def slidingWindow(nums = [4,-1,2,-7,3,4]):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    left = 0
    for right in range(len(nums)):
        if curSum < 0:
            curSum = 0
            left = right
        curSum += nums[right]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = left, right
    return [maxL, maxR]
