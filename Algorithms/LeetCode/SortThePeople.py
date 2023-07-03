
# My Solution
def SortThePeople(names = ["Mary","John","Emma"], heights = [180,165,170]):
    a = sorted(zip(heights, names))
    res = []
    for i, j in a:
        res.append(j)
    print(res[::-1])            
SortThePeople()

