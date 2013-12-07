from sys import stdin, stdout
from string import rstrip

def failsum(numbers):
    total = 0
    for number in numbers: total=total^number
    return total
input = []
for line in stdin:
    input.append(rstrip(line,'\n'))
nTestCases = int(input[0])
line = 1
while line < len(input):
    candies = input[line+1].split(' ')
    candies = [int(candy) for candy in candies]
    if failsum(candies)%2: stdout.write("Case #%s: NO\n"%((line+1)/2))
    else: stdout.write("Case #%s: "%((line+1)/2)+str(sum(candies)-min(candies))+'\n')
    line += 2

