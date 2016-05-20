import random

n = 1000

cs = [[0 for _ in range(n)] for __ in range(n)]

for __ in range(100000):
    a = [k for k in range(n)]

    for k in range(n):
        p = random.randint(0, n - 1)
        s = a[p]
        a[p] = a[k]
        a[k] = s

    for i, x in enumerate(a):
        cs[i][x] += 1

print str(cs).replace('[','{').replace(']','}')