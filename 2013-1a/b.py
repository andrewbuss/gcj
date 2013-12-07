from sys import stdin, stdout
lines = stdin.read().split('\n')
ntests = int(lines.pop(0))

for test in range(ntests):
    stdout.write("Case #"+str(test+1)+": ")
    e,r,n = map(int,lines.pop(0).split(' '))
    r = min(e,r)
    vs = map(int,lines.pop(0).split(' '))
    g = sum(vs)*r
    print "E:", e, "R:", r, "N:", n
    print "Lower gain bound:", g
    v = e
    right = vs
    left = []
    sl = []
    while right:
    	cur = right.pop(0)
    	print left, cur, right
    	sl.append(v)
    	left.append(cur)
    	v=r
    print g