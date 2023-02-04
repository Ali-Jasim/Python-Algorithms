def pal(s):
    high = len(s)-1
    low = 0

    while low < high:
        if s[high] != s[low]:
            return False
        low = low+1
        high = high-1

    return True


def python_pal(s):
    if s == s[::-1]:
        return True

    return False


s = "car"
print(pal(s))
print(python_pal(s))
