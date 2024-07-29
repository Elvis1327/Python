

def uniqueOccurrences( arr = [1,2,2,1,1,3] ):
    countT = {}
    for num in arr:
        if num in countT:
            countT[num] += 1
        else:
            countT[num] = 1
    if len(countT.values()) == len(set(countT.values())):
        return True
    return False

