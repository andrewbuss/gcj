from collections import defaultdict

T = int(raw_input())
N = 0
c = []
bffs = []
m = 0
avail = []


def verify(s):
    global m
    s = [s[-1]] + s + [s[0]]
    # for i in range(1, len(s) - 1):
    #     assert s[i - 1] == bffs[s[i]] or s[i + 1] == bffs[s[i]]
    m = max(m, len(s) - 2)


def solve2(i):
    global m, L, c
    b = bffs[i]
    # print '   ' * len(c), i, b, c
    if c and b == c[0]:
        # print '   ' * len(c), "Found full loop", c + [i]
        verify(c + [i])
    if c and b == c[-1]:
        avail[i] = 0
        c.append(i)
        verify(c)
        # print '   ' * len(c), "Found half loop", c
        solve()
        c.pop(-1)
        avail[i] = 1
    else:
        if not avail[b]:
            return
        avail[i] = 0
        c.append(i)
        solve2(b)
        c.pop(-1)
        avail[i] = 1


def solve():
    for x in range(N):
        if not avail[x]: continue
        print '   ' * len(c),
        print "Start with", x
        solve2(x)
        if m == N: return


for t in range(T):
    N = int(raw_input())
    counts = defaultdict(int)
    m = 0
    bffs = map(lambda x: int(x) - 1, raw_input().split())
    avail = range(N)
    for i in range(N):
        avail[i] = 1
    solve()
    print "Case #%d:" % (t + 1), m
    s = 0
