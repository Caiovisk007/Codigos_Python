def fat(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

for i in range(5) : print (fat(i))