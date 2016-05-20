from sys import stdin

lines = stdin.read().replace('\r', '').split('\n')

T = int(lines.pop(0))

for CN in range(1, T + 1):
    n = int(lines.pop(0))
    p = map(int, lines.pop(0).split(" "))
    print "Case #%d:" % CN,