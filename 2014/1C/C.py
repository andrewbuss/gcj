from sys import stdin

lines = stdin.read().replace('\r', '').split('\n')

T = int(lines.pop(0))

cd = {}


def coverage(n, m):
    if n * 1001 + m not in cd: cd[n * 1001 + m] = n * m + 2 * m + 2 * n
    return cd[n * 1001 + m]


def solve(n, m, k):
    if m > n: n, m = m, n
    print n, m, k
    best = 1000000
    for nn in range(1, n):
        for mn in range(1, m):
            c = coverage(nn, mn)
            i = nn * 2 + mn * 2
            for r in range(mn):
                c -= r
                print nn, mn, r, c, i
                if c < k: break
                best = min(i, best)
                i -= 1
                c -= 1
    return min(k, best)


for CN in range(1, T + 1):
    print "Case #%d:" % CN, solve(*map(int, lines.pop(0).split(' ')))

