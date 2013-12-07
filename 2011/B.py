from sys import stdin, stdout
from string import rstrip

input = []
for line in stdin:
    input.append(rstrip(line,'\n'))

nTestCases = int(input.pop(0))

for line in input:
    tokens = line.split(' ')
    C = int(tokens.pop(0))
    combos = tokens[0:C]
    combos = [[''.join(list(combo)[0:2]),list(combo)[2]] for combo in combos]
    tokens = tokens[C:len(tokens)]
    D = int(tokens.pop(0))
    opposed = [list(oppose) for oppose in tokens[0:D]]
    tokens = tokens[D:len(tokens)]
    N = int(tokens.pop(0))
    elq = tokens[0]
    ell = []
    for el in elq:
        ell.append(el)
        if len(ell) < 2:  continue
        tail = [ell.pop(len(ell)-2), ell.pop()]
        replaced = False
        for combo in combos:
            if combo[0] == ''.join(tail):
                ell.append(combo[1])
                replaced = True
                break
            elif combo[0][::-1] == ''.join(tail):
                ell.append(combo[1])
                replaced = True
                break
        if not replaced: ell.extend(tail)
        for oppose in opposed:
            if ell.count(oppose[0]) > 0 and ell.count(oppose[1]) > 0:
                ell = []
                continue
    ells = str(ell).translate(None,"'")
    stdout.write("Case #%s: "%line+ells+'\n')
    line += 1

