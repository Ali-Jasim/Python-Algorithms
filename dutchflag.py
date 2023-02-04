
def sort(l, mid):
    i = 0
    j = 0
    k = len(l)-1

    while k >= j:
        if l[j] > mid:
            l[k], l[j] = l[j], l[k]
            k = k - 1
        if l[j] < mid:
            l[i], l[j] = l[j], l[i]
            j = j + 1
            i = i + 1
        if l[j] == mid:
            j = j + 1


a = [1, 2, 2, 0, 1, 2, 0]

sort(a, 1)

print(a)
