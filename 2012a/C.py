from collections import deque
from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[testcase-1].split(' ')
    A = int(tokens.pop(0))
    B = int(tokens.pop(0))
    A = 1000000
    B = 2000000
    dr = 0
    m = 0
    digits = len(str(A))
    for n in xrange(A,B):
        if not n%10000: print n
        sn = str(n)
        ms = [-1 for _ in range(8)]
        #print n,
        for i in range(1,digits):
            m = int(sn[i:digits+1])*(10**i)+int(sn[0:i])
            #print m,
            if m in ms: break
            else: ms[i] = m
            if n < m <= B: dr += 1
        #print
    stdout.write(str(dr)+"\n")
    if testcase >= nTestCases: break
    testcase +=1

