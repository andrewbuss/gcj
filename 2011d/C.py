from sys import stdin, stdout
from string import rstrip

notes = []
def product(list):
    t = 1
    for n in list: t *= n
    return t
def factor(n):
    if n == 1: return [1]
    i = 2
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            ret = factor(n/i)
            ret.append(i)
            return ret
        i += 1
    return [n]
def gcd(a,b):
    while b: a, b = b, a % b
    return a
def lcm(a,b): return (a*b)/gcd(a,b)
def GCD(terms):return reduce(lambda a,b: gcd(a,b), terms)
def LCM(terms): return reduce(lambda a,b: lcm(a,b), terms)
def topmod(p): return [n%p for n in notes]
def bottommod(p): return [p%n for n in notes]

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))
testcase = 1
line = 0

while True:
    stdout.write("Case #%s: "%testcase)
    tokens = input[line].split(' ')
    N = int(tokens[0])
    L = int(tokens[1])
    H = int(tokens[2])
    notes = input[line+1].split(' ')
    notes = [int(note) for note in notes]
    notes.sort()
    p = notes[0]
    i = 0
    result = -1
    while True:
        note = notes[i]
        t = topmod(p)
        b = bottommod(p)
        bmk = 0
        for bmk, bm in enumerate(b):
            if bm: break
        i = bmk
        p *= notes[bmk]
        if p>H: break
        if p<L: continue
        if i>len(notes): break
        if not max(t[i:]):
            result = p
            break
    if result == -1: stdout.write('NO\n')
    else: stdout.write(str(result)+'\n')
    line += 2
    testcase += 1
    if testcase > nTestCases: break