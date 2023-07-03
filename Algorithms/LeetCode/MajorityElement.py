

def majorityElement(nums = [3,2,3]):
        # Initialize a HashTable
        hash = {}
        # Loop through the Array
        for i in nums:
            # This line is very important beacause is the same as the code down
            # if i not in hash:
            #      hash[i] = 0
            # hash[i] += 1
            # So this line we compute each num of the array as a key on the hash table and sum plus 1 is repited
            hash[i] = hash.get(i,0) + 1
        for k, j in hash.items():
            # k is the key of the hashTable and j is the value
            if j > len(nums) // 2:
                return k


