

# I loop through all elements and then created Another loop
# to compare all the elements and the array then with the variable count we sum plus 1 
# if we find one element which nums[i] > nums[j] we append count to the new variable 
# result 
def smallerNumbersThanCurrent(nums = [8,1,2,2,3]):
    count = 0
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            print(i,j)
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
smallerNumbersThanCurrent()