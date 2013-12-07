from string import rstrip
from sys import stdin, stdout

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
d = 0

def prod(m):
    result = 1
    for i in m: result *= i
    return result

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input.pop(0).split(' ')
    a = int(tokens.pop(0))
    b = int(tokens.pop(0))
    p = []
    tokens = input.pop(0).split(' ')
    for _ in xrange(a): p.append(float(tokens.pop(0)))
    print a,b, p
    pincorrect = 1-prod(p)
    eincorrect = pincorrect*(2*b-a+2)+(1-pincorrect)*(b-a+1)
    print pincorrect, eincorrect, min(eincorrect,2+b)
    stdout.write("\n")
    if testcase >= nTestCases: break
    testcase +=1
