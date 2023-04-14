

# Sorting Algorithms are very important because they help us to better understand how to manipulate Arrays

# Bubble Sort Algorithm
numsbubbleSort = [7,2,5,9,5,1,6,3]
def bubbleSort(nums = numsbubbleSort):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            # If we put (- i) in the second loop this will reduce one loop for each trouhgt example
            # [0,3,2,1,], [0,2,1] [0,1], [0]
            if nums[j] > nums[j+1]:
                # Swap
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp

# ********************************

# Selection Sort Algoritm
numsSelectionSort = [34,22,10,19,17]
def selectionSort(nums = numsSelectionSort):

    for i in range(len(nums)):

        lowestMin = i
        
        print("PRIMER LOOP")

        for j in range(i + 1,len(nums)):
            print('SEGUNDO LOOP')
            print(j)
            if nums[j] < nums[lowestMin]:
                lowestMin = j
                print("PASO")
            print('AFTER IF')

        temp = nums[i]
        nums[i] = nums[lowestMin]
        nums[lowestMin] = temp
        print('REPITE TODO')

# ***********************************

# Selection Sort
# numsInsertionSort = [34,22,10,19,17]
numsInsertionSort = [2,6,5,1,3,4]
def insertionSort(nums = numsInsertionSort):
    for i in range(1, len(nums)):
        j = i
        print('"I PRINCIPIO')
        while nums[j - 1] > nums[j] and j > 0:
            print('J ANTES DEL SWAP', j)
            temp = nums[j]
            nums[j] = nums[j-1]
            nums[j-1] = temp
            print(j)
            print("J DESPUES DEL SWAP", j)
            j -= 1
            print("J DESPUES DE TODO", j)
    # print(nums)
insertionSort()


