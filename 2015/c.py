replacements = {}

lut = [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]
sign = [[0,0,0,0],[0,1,0,1],[0,1,1,0],[0,0,1,1]]

def evaluate(x):
    if x in replacements: return replacements[x]
    if len(set(x)) == 1:
        if len(x)%2: replacements[x] = x[0]
        else: replacements[x] = 0
        return replacements[x]
    s = 0
    c = 0
    for i in x:
        s ^= sign[c][i]
        c = lut[c][i]
    if s: c = 0
    replacements[x] = c
    return replacements[x]

    

import sys

lines = sys.stdin.read().split('\n')
T = int(lines.pop(0))
tn = 0
while lines[0]:
    tn += 1
    L, X = map(int, lines.pop(0).split(' '))
    s = lines.pop(0)*X
    s = tuple(map('1ijk'.index, s))
    done = 0
    for a in range(1,len(s)-1):
        if evaluate(s[:a]) != 1: continue
        ab = 0
        sab = 0
        for b in range(a, len(s)):
            sab ^= sign[ab][s[b]]
            ab = lut[ab][s[b]]
            #print 'a =', a, 'b =', b, 'ab =',ab, 'sab =',sab
            if ab == 2 and sab == 0:
                if evaluate(s[b+1:]) == 3:
                    print 'Case #%d: YES'%tn
                    done = 1
                    break
        if done: break
    if not done:
        print 'Case #%d: NO'%tn
