

# Longest Substring with at mostt two distinct characters




def test(n):
    if n <= 1:
        return n
    return test(n - 1) + test(n - 2)

print(test(5))

