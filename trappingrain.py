def trapping_rain(l):
    max_left = []
    max_right = []
    trapped = []

    max_val = 0
    for i in range(len(l)):
        if max_val < l[i]:
            max_val = l[i]
        max_left.append(max_val)

    max_val = 0
    for i in range(len(l)-1, -1, -1):
        if max_val < l[i]:
            max_val = l[i]
        max_right.append(max_val)

    for i in range(len(l)):
        wall = min(max_left[i], max_right[i])
        amount = wall - l[i]
        trapped.append(amount)

    print(trapped)

    return sum(trapped)


a = [1, 0, 3, 0, 3, 0, 2, 1, 5]
c = [1, 0, 2, 1, 3, 1, 2, 0, 3]

b = trapping_rain(c)

print(b)
