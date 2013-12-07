from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input.pop(0).split(' ')
    N = int(tokens.pop(0))
    M = int(tokens.pop(0))
    tokens = input.pop(0).split(' ')
    boxes = []
    for i in xrange(N): boxes.append((int(tokens.pop(0)),int(tokens.pop(0))))
    tokens = input.pop(0).split(' ')
    toys = []
    for i in xrange(M): toys.append((int(tokens.pop(0)),int(tokens.pop(0))))
    print boxes
    print toys
    i = 0
    if boxes[i][1] != toys[i][1]:

    stdout.write("\n")
    if testcase >= nTestCases: break
    testcase +=1
