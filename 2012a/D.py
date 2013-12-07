from string import rstrip
from math import sin, cos, pi
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
mirrors = []

def intersected(v):
    for

while input:
    mirrors = []
    stdout.write("Case #%s: "%testcase)
    tokens = input.pop(0).split(' ')
    H = int(tokens.pop(0))
    W = int(tokens.pop(0))
    D = int(tokens.pop(0))
    m = ''
    while len(m)<H*W:
        m+=input.pop(0)
    print H,W,D
    o = (m.find('X')%H+0.5,m.find('X')/W+0.5)
    print o
    for y in range(H):
        for x in range(W):
            if m[y*W+x] == '#': mirrors.append((x,H-y-1))
            stdout.write(m[y*W+x])
        print
    print mirrors
    va = o+(1,0)
    vb = o+(-1,0)
    testcase +=1

