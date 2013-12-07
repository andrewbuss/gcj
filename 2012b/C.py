from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
d = 0

while True:
    stdout.write("Case #%s: "%testcase)
    n = int(input.pop(0))
    lines = []
    for _ in xrange(n):
        tokens = input.pop(0).split(' ')
        lines.append([int(tokens[1]),int(tokens[2])])
    print lines
    for la,a in enumerate(lines):
        for lb,b in enumerate(lines):
            print a,b,
            if a == b or line[0] == [0]: continue
            y = (-line2[1]*line[0]+line[1]*line2[0])/(line[0]-line2[0])
            x = (line[1]-line2[1])/(line[0]-line2[0])
            print x,y
    stdout.write("\n")
    if testcase >= nTestCases: break
    testcase +=1
