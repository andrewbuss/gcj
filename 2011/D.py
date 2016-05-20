from sys import stdin, stdout
from string import rstrip

input = []
for line in stdin:
    input.append(rstrip(line,'\n'))
nTestCases = int(input[0])
line = 1
while line < len(input):
    stones = input[line+1].split(' ')
    outofplace = 0
    for i in range(len(stones)):
        if i+1 != stones[i]: outofplace += 1
