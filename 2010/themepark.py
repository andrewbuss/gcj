import re
from collections import deque
filename = 'C-small-practice4'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
ntestcases = infile.readline().rstrip()
print "Solving", ntestcases, "test cases.\n"
i=0
results=[]
def solve(i, r, k, n, g=[]):
    if n==1:
        nf = "1 group."
    else:
        nf = str(n)+" groups."
    print "Solving test case #"+str(i), "with", str(r), "rides,", k, "capacity, and", nf
    print "   Group(s):", g
    if sum(g)<=k:
        totalincome = sum(g)*r
        print "   Easy way found. Because the total number of riders is less than or equal to\n   the capacity of a single ride, I deduce that", sum(g), "total riders riding \n  ", r, "times brings in", totalincome, "euros.\n"
        return totalincome
    if r<n:
        income=0
        print "   Easy way found. Because R < N, and N < 1000,\n   it is fast enough to run the full simulation without optimization."
        g = deque(g)
        income = 0 
        while r > 0:
            remainingspots = k
            gi = 0
            while True:
                if g[gi] <= remainingspots:
                    remainingspots=remainingspots-g[gi]
                    income = income+g[gi]
                    gi = gi+1
                else:
                    break
            g.rotate(-gi)
            r = r - 1
        print "   Total income of test case", str(i)+":", income, "euros\n"
        return income
    g = deque(g)
    initialincome = 0
    remainingspots = k
    gi = 0
    while True:
        if g[gi] <= remainingspots:
            remainingspots=remainingspots-g[gi]
            initialincome = initialincome+g[gi]
            gi = gi+1
        else:
            break
    g.rotate(-gi)
    print "   Initial income =", initialincome
    ridenum = 1
    secondaryincome = 0
    if n<r:
        p = r
    elif n==r:
        p = n
    while ridenum < p:
        remainingspots = k
        gi = 0
        while True:
            if g[gi] <= remainingspots:
                remainingspots=remainingspots-g[gi]
                secondaryincome = secondaryincome+g[gi]
                gi = gi+1
            else:
                break
        g.rotate(-gi)
        ridenum = ridenum+1
    print "   Secondary income:", secondaryincome
    totalincome = (((r-1)/(n-1))*secondaryincome)+initialincome
    print "   Total income of test case", str(i)+":", totalincome, "euros\n"
    return totalincome

while i<int(ntestcases):
    firstline=infile.readline()
    secondline=infile.readline()
    firstline = firstline.rstrip()
    secondline = secondline.rstrip()
    parsedfirstline = re.split(":? ", firstline, 3)
    secondline = re.split(":? ", secondline, 1000)
    parsedsecondline=[]
    for gi in secondline:
        parsedsecondline.append(int(gi))
    results.append(solve(i+1, int(parsedfirstline[0]),int(parsedfirstline[1]),int(parsedfirstline[2]),parsedsecondline))
    i=i+1
    
formattedresults = ""
for casenum in range(0,int(ntestcases)):
    formattedresults = formattedresults + "Case #" + str(casenum+1) + ": " + str(results[casenum]) + "\n"

print "\n  Results:"
print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done."
outfile.close()
infile.close()
