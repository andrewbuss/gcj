import re
import math
filename = 'A-small-practice'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
print infile
ntestcases = infile.readline(5)
print infile.readline()
print "Solving", ntestcases, "test cases."
i=0
results=[]

def solve(i,n,k):
    #print "Solving test case #" + str(i)+" with", n, "snappers and", k, "snaps."
    state = 0
    if k % (2^n-1) == 0:
        return 'ON'
    else:
        return 'OFF'
        
while i<int(ntestcases):
    line=infile.readline()
    line = line.rstrip()
    parsedline = re.split(":? ", line, 2)
    results.append(solve(i+1, int(parsedline[0]),int(parsedline[1])))
    i=i+1
    
formattedresults = ""
for casenum in range(0,int(ntestcases)):
    formattedresults = formattedresults + "Case #" + str(casenum+1) + ": " + results[casenum] + "\n"

print "\n  Results:"
print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done."
outfile.close()
