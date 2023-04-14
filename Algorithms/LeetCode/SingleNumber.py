
# Single Number question from Leetcode so the question says that given an integrer array find the number 
# that does not appears two times.
# In this approach I used brute force approach and used HashMap Datastructure
# I compute all the nums as a Key in the hashmap and initialize the values as 0 for each key if the key appears two or more
# times we sum up plus 1 the value of the key
# the final loop we compare if the Key has a value less or equal than 1 we return that key.
def singleNumber(nums = [4,1,2,1,2]):
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 0
            hash[i] += 1
        for j, f in hash.items():
            print(j, f)
            if hash[j] <= 1:
                 return j
singleNumber()