# SLIDING WINDOW
# Return a subArray of size 3 which if we sum the subArray is the result of the sum of target
# This example was implemented by me
def slidingWindow(elements = [1,2,10,10,10,6,7,8], size = 3, target = 30 ):
    result = None
    if len(elements) <= size:
        return elements
    for i in range(len(elements) - size + 1):
        if sum(elements[i:size + i]) == target:
            result = elements[i:size+i]
    return result
print(slidingWindow())