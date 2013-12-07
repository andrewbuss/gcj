from sys import stdin, stdout
from string import rstrip

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
line = 0

while True:
    tokens = input[line].split(' ')
    C = int(tokens[0])
    D = float(tokens[1])
    totallength = 0
    points = [[float(j) for j in i.split(' ')] for i in input[line+1:line+C+1]]
    vs = [[point[0]*point[1]][0] for point in points]
    time = 0
    for i in range(1,len(vs)):
        v = vs[i] 
        if v-vs[i-1] <= D:
            vs[i] = vs[i-1]+D
            time = max(time,vs[i]-v)
    stdout.write("Case #%s: "%testcase+str(time/2)+'\n')
    line += C+1
    testcase += 1
    if testcase > nTestCases: break