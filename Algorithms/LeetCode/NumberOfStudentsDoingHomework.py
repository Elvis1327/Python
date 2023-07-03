
# My Solution
def busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4):
    count = 0
    for i in range(len(startTime)):
        # If statement to see if the queryTime is beetwen startTime and endTime
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            count += 1
    return count


