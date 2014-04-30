import string
import time
import sys
filename = 'B-small-practice'
infilename = filename+'.in'
outfilename = filename+'.out'
infile = open(infilename,'r')
outfile = open(outfilename,'w')
print infile
ntestcases = int(infile.readline(4).rstrip())
#ntestcases = 1
print "Solving", ntestcases, "test cases.\n"
results, hm = [],[]

def printmap(pm):
    h = len(pm)
    w = len(pm[0])
    fr = ''
    for rownum in range(0,h):
        trow = ''
        for colnum in range(0,w):
            trow += str(pm[rownum][colnum])
        fr += (trow+'\n')
    print fr

def evaluate(row, col):
    if r[row][col] != 0:
        return 0
    global r
    global m
    la = 10000
    a = m[row][col]
    h = len(m)
    w = len(m[0])
    try:
        if m[row+1][col] < la:
            la=m[row+1][col];ld='s'
    except:pass

    try:
        if m[row][col+1] < la:
            la=m[row][col+1];ld='e'
    except:pass
    
    if m[row][col-1] < la and col > 0:
        la=m[row][col-1];ld='w'
    if m[row-1][col] < la and row > 0:
        la=m[row-1][col];ld='n'
    if la < a:
        if ld == 'n':
            evaluate(row-1,col)
            r[row][col] = r[row-1][col]
        elif ld == 'w':
            evaluate(row,col-1)
            r[row][col] = r[row][col-1]
        elif ld == 'e':
            evaluate(row,col+1)
            r[row][col] = r[row][col+1]
        elif ld == 's':
            evaluate(row+1,col)
            r[row][col] = r[row+1][col]            
    else:
        global nl
        r[row][col] = nl
        nl += 1

starttime = time.time()

while ntestcases > 0:
    dline = string.split(infile.readline().rstrip())
    h,w = int(dline[0]),int(dline[1])
    r,m = [],[]
    nl = 97
    [m.append([int(x) for x in string.split(infile.readline().rstrip())]) for rownum in range(0,h)]
    hm.append(m)
    [r.append([0 for col in range(0,w)]) for row in range(0,h)];
    printmap(m)
    [evaluate(row, col) for col in range(0,w) for row in range(0,h)]
    results.append(r)
    ntestcases -= 1
    
endtime = time.time()
for cn in range(0,ntestcases):
    printmap(hm[cn])
    printmap(results[cn])
    
formattedresults = ""
casenum = 1
for case in results:
    formattedresults = formattedresults + "Case #" + str(casenum) + ":\n" 
    for row in case:
        trow = ''
        for col in row:
            trow += (chr(col) + ' ')
        formattedresults = formattedresults + trow + "\n"
    casenum +=1

#print "Results of watershed analysis of", ntestcases, "test cases from", infilename,":"
#print formattedresults
print "Writing results to", outfilename
print outfile
outfile.write(formattedresults)
print "Done. Solved in", endtime-starttime,"seconds."
infile.close()
outfile.close()
