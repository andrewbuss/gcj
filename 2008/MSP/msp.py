from sys import stdin, stdout, stderr
from string import rstrip
from mspsolve import solve

input = []
for line in stdin:
    input.append(rstrip(line,'\n'))

nTestCases = int(input[0])
stdout.write("# %s test cases\n"%nTestCases)

line = 1
while line < len(input):
    n = input[line]
    v1 = [int(token) for token in input[line+1].split(' ')]
    v2 = [int(token) for token in input[line+2].split(' ')]
    stderr.write('# Case '+str((line+2)/3)+'\n')
    stderr.write('# %s-dimensional vectors:\n'%n)
    stderr.write('# v1: '+str(v1)+'\n')
    stderr.write('# v2: '+str(v2)+'\n')
    stderr.write('# Minimum Scalar Product:\n')
    msp = str(solve(n, v1, v2))
    stderr.write('# '+msp)
    stderr.write('############################\n')
    stdout.write("Case # %s: "%((line+2)/3)+msp+'\n')
    line += 3