

# Longest Substring with at mostt two distinct characters




def test(n):
    if n <= 1:
        return n
    return test(n - 1) + test(n - 2)

print(test(5))

string = "ab"
res = []
res.append(string[0:2])


test = ""
res2 = test + string


res = True and True
print(res)



