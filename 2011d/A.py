from sys import stdin, stdout
from string import rstrip

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
line = 0

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[line].split(' ')
    answer = 0
    stdout.write(str(answer/2)+'\n')
    line += C+1
    testcase += 1
    if testcase > nTestCases: break