from string import rstrip
from sys import stdin, stdout, setrecursionlimit

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
setrecursionlimit(2000)

def findnodes(node):
    visited[node] = 1
    for c in cs[node]:
        if visited[c] or findnodes(c): return 1
    return 0

while 1:
    stdout.write("Case #%s: "%testcase)
    tokens = input.pop(0).split(' ')
    N = int(tokens.pop(0))
    cs = [[] for _ in xrange(N)]
    for i in xrange(N):
        tokens = input.pop(0).split(' ')
        tokens.pop(0)
        for _ in tokens: cs[i].append(int(_)-1)
    for i in xrange(N): cs[i] = sorted(cs[i])
    found = 0
    visited = [0 for _ in xrange(N)]
    for i in xrange(N):
        if not cs[i]: continue
        visited = [0 for _ in xrange(N)]
        if findnodes(i):
            found = 1
            break
    if found: stdout.write("Yes\n")
    else: stdout.write("No\n")
    if testcase >= nTestCases: break
    testcase +=1
