

def distributeCandies(candyType = [1,1,2,2,3,3]):
    candies = 1
    for i in range(1,len(candyType)):
        if candyType[i] != candyType[i-1]:
            candies += 1
    return min(candies, len(candyType) // 2)

# Second option less code faster

def distributeCandies(candyType = [1,1,2,2,3,3]):
    res = set(candyType)
    return min(len(res), len(candyType) // 2)




