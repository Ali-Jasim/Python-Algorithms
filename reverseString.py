li = [1, 2, 3, 4, 5]


def reverse(l):
    high = len(l)-1
    low = 0

    while low < high:
        l[high], l[low] = l[low], l[high]
        low = low+1
        high = high-1


reverse(li)
print(li)
