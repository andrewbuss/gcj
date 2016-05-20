from itertools import permutations
from sys import stdin

lines = stdin.read().replace('\r', '').split('\n')

T = int(lines.pop(0))


def compact(s):
    o = ''
    cur = ''
    for c in s:
        if c != cur: o += c
        cur = c
    return o

def nchars(s):
    sn = set()
    for c in s:
        sn.add(c)
    return len(sn)

for CN in range(1, T + 1):
    n = int(lines.pop(0))
    a = lines.pop(0).split(' ')
    a = map(compact, a)
    d = {}
    starts = set()
    ends = set()
    valid = 0
    for s in permutations(a):
        s = ''.join(s)
        if len(compact(s)) == nchars(s): valid += 1
    print "Case #%d:" % CN, valid