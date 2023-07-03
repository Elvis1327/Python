
# Looked for the solution
def differenceOfSum(nums = [1,15,6,3]):
    digit_sum = 0
    for i in nums:
        for j in str(i):
            digit_sum += int(j)
    return sum(nums) - digit_sum
