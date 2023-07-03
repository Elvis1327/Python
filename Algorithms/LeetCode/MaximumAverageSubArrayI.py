


# I READ THE SOLUTION TRY TO UNDERSTAND AND LEARN   
def findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4):
    left = 0
    currentSum = sum(nums[0:k])
    maxSum = currentSum
    for right in range(k, len(nums)):
        currentSum = currentSum + nums[right] - nums[right - k]
        maxSum = max(currentSum, maxSum)
    return maxSum / k

# ***********
# MY OWN SOLUTION FIXED SIZE SLIDING WINDOW
# ***************
def findMaxAverageMySolutionSlidingWindow(nums = [1,12,-5,-6,50,3], k = 4):
    # Iniciate two pointers (l, r) 
    # and current is the first sum of the array of size k
    # then (r - l + 1) this is the line of sliding window
    l, current = 0, sum(nums[0:k])
    maxSum = current
    for r in range(k, len(nums)):
        if (r - l + 1) > k:
            current = current - nums[l]
            l += 1
        current = current + nums[r]
        maxSum = max(maxSum, current)
    return maxSum / k



