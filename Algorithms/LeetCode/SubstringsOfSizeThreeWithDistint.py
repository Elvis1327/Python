


# Solution Sliding Window
def countGoodSubstrings(s = "xyzzaz"):
    size = 3
    res = 0
    for i in range(len(s) - size + 1):
        window = s[i:size+i]
        if len(set(window)) == 3:
            res += 1
    return res 
