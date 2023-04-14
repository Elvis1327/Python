

# we need to Concatenar 2 So this was my first Approach create a valiable giving the value of the Array
# and then iterate for each value on nums and finally pushing each value to the Array Ans.
def getConcatenation(nums=[1,2,1]):
    ans = nums
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans

# ***************

# I Liked this different approach using Extend() method.
# The extend() method adds all the element of an iterable ( list , tuple , string etc.) to the end of the list.
def getConcatenationExtend(nums=[1,2,1]):
        nums.extend(nums)
        return nums