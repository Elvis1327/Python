

def sortedArray(array):
    sortValues = [0 for _ in array]
    for value in range(len(array)):
        data = array[value]
        sortValues[value] = data * data
    sortValues.sort()
    return sortValues

# print(sortedArray([1,2,3,4,5]))
sortedArray([1,2,3,4,5])
