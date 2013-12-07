from sys import stdin, stdout
lines = stdin.read().split('\n')
ntests = int(lines.pop(0))
chests =[]
keys = set()

def bs(mks, mcs):
    #print "Bs,",mks,mcs
    if len(mcs) == len(chests): return mcs
    for i in range(len(chests)):
        #print i
        if (i in mcs) or (not mks[chests[i][0]]): continue
        ncs = list(mcs) + [i]
        nks = list(mks)
        for key in chests[i][2]: nks[key]+=1
        nks[chests[i][0]]-=1
        rv = bs(nks,ncs)
        if rv: return rv

for test in range(ntests):
    k,n = map(int,lines.pop(0).split(' '))
    ks = map(int,lines.pop(0).split(' '))
    print "starting with", ks
    chests =[]
    nks=[0]*26
    for key in ks: nks[key]+=1
    for chest in range(n):
        line = map(int,lines.pop(0).split(' '))
        chests.append([line[0],line[1],line[2:]])
    print chests
    rv = bs(nks,[])
    if rv: 
        rv = map(lambda x:x+1,rv)
        stdout.write("Case #"+str(test+1)+": "+' '.join(map(str,rv))+'\n')
    else: stdout.write("IMPOSSIBLE\n")