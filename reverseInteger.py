

def reverse(i):
    newi = 0

    while i != 0:
        newi = newi*10
        newi = newi+(i % 10)
        i = i//10
       # i = int(i/10)

    return newi


t = 9999933333
b = reverse(t)
print(t)
print(b)
