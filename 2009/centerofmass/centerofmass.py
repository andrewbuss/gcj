import re
filename = 'B-test'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
print infile
ntestcases = infile.readline(4).rstrip()
print "Solving", ntestcases, "test cases.\n"
i=0
results=[]
from math import sqrt

def solve(i,n,x,y,z,vx,vy,vz):
    dmin = 10**10
    tmin = 10**10
    print "Solving test case", i, "with", n, "fireflies."
    print "   Solving for center of mass at t=0:"
    ix = sum(x)/n
    iy = sum(y)/n
    iz = sum(z)/n
    print "    ("+str(ix)+",",str(iy)+",",str(iz)+")"
    print "   Solving for velocity of mass at t=0:"
    ivx = sum(vx)/n
    ivy = sum(vy)/n
    ivz = sum(vz)/n
    print "    ("+str(ivx)+",",str(ivy)+",",str(ivz)+")"
    print "   Solving for minimum distance:"
    t=0
    while True:
        t += 10**(-1)
        cx = t*ivx+ix
        print cx
        cy = t*ivy+iy
        cz = t*ivz+iz
        d = sqrt(cx*cx+cy*cy+cz*cz)
        print t
        print d
        if d < dmin:
            dmin = d
        elif d > dmin:
            print '       Found larger distance, concluding that previous distance is minimum.'
            print '       Previous distance at t =',str(t-10**(-5))+':', dmin
            return dmin, t-10**(-5)

while i<int(ntestcases):
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    numfireflies = int(infile.readline().rstrip())
    for fireflynum in range(0,numfireflies):
        line = re.split(":? ", infile.readline().rstrip(), 6)
        x.append(int(line[0]))
        y.append(int(line[1]))
        z.append(int(line[2]))
        vx.append(int(line[3]))
        vy.append(int(line[4]))
        vz.append(int(line[5]))
        
    results.append(solve(i+1,numfireflies,x,y,z,vx,vy,vz))
    i=i+1
    
formattedresults = ""
for casenum in range(0,int(ntestcases)):
    formattedresults = formattedresults + "Case #" + str(casenum+1) + ": " + str(dmin) + ' ' + str(tmin) + '\n'

print "\nResults of analysis of", ntestcases, "test cases from", infilename,":\n"
print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done."
outfile.close()
