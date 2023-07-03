

def isAnagram( s = "anagram", t = "nagaram" ):

    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for j in countS:
        # when we say " for j in countS: " this line of code is going to iterate over the keys, no over the values so the j is equal to the keys, like (a,n,g,r,m)
        # the " countT.get(j,0) " is in case a KEY of countS does not exits in countT 
        if countS[j] != countT.get(j, 0):
            return False
    
isAnagram()
