import re
filename = 'B-small-practice'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
print infile
outfile = open(outfilename,'w')
ntestcases = infile.readline().rstrip()
print "Solving", ntestcases, "test cases.\n"
i=0
results=[]


def Gcd(a, b):
  if b == 0:
    return a
  return Gcd(b, a % b)

def Solve(i, n, L):
  print "Solving test case", i, "with", n, "Great Events. Great events:"
  print "  ", L
  y = L[0]
  L1 = [abs(x - y) for x in L]
  g = reduce(Gcd, L1)
  if y % g == 0:
    print "   Result : 0"
    return 0
  else:
    print "   Result :", g - (n % g)
    return g - (y % g)

while i<int(ntestcases):
    line=infile.readline()
    line = re.split(":? ", line, 1001)
    greatevents = []
    for event in range(0,len(line)):
        greatevents.append(int(line[event].rstrip()))
    results.append(Solve(i+1, int(line[0]), greatevents))
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
