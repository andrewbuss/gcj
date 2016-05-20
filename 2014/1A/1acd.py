import random

n = 1000


def ana(r):
    t = 0
    for i in range(n):
        if i < r[i] < i + 300:
            t += 1
    return t


ts = []

for _ in range(100):
    p = [k for k in range(n)]

    for k in range(n):
        x = random.randint(0, n - 1)
        s = p[x]
        p[x] = p[k]
        p[k] = s

    ts.append(ana(p))

print ts, sum(ts)/len(ts)
ts = []
for _ in range(100):
    p = [k for k in range(n)]
    random.shuffle(p)
    ts.append(ana(p))
print ts, sum(ts)/len(ts)


