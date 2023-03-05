
input = [1,1,1,1,1,2,2,2,2,3,3,5,]

def conuntUniqueValues(input):
    l = 0
    r = len(input) - 1
    result = 0
    while l < r:
        if input[l] != input[r]:
            result = result + 1
        l = l + 1
        r = r -1
    print(result)

conuntUniqueValues(input)


         