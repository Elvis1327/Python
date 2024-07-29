

# SLIDING WINDOW PROBLEM
def lengthOfLongestSubstringKDistinct(self, s = "eceba", k = 2):
    # We create a hashTable to track the length 
    charS = {}
    # Left pointer
    left = 0
    # Max LongestSubstring
    longSubs = 0
    # Start looping 
    for right in range(len(s)):
        # We add a string as a key of the hashTable and a number as a value of 
        # the hashTable
        charS[s[right]] = charS.get(s[right], 0) + 1
        # While the length of the hashTable is greater than k
        # we need to substrack the first element
        while len(charS) > k:
            # This is very important here because we need to check
            # if the element is greater than one in the hashMap
            # then we -= 1 and sum up one value to the left pointer.
            if charS[s[left]] > 1:
                charS[s[left] ] -= 1
                left += 1
            else:
                # Here we delete the character of the hashMap and sumup
                # one value more to the left pointer.
                del charS[s[left]]
                left += 1
        # Here we compute the indice of the right and left pointer.
        longSubs = max(longSubs, right - left + 1)
    return longSubs
