
def anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    visited = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if j in visited:
                continue
            elif s1[i] == s2[j]:
                visited.append(j)

    print(visited)
    print(s2)

    return len(visited) == len(s1)


def better(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


a = "stupid77"
b = "d77ipstu"

print(better(a, b))
