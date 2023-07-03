

nums = [2,5,5,11]
target = 10
def twoSums(nums, target):
    for i in range(len(nums - 1)):
        for j in range(i+1 ,len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i,j]


def shuffle():