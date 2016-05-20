from sys import stdin, stdout
from string import rstrip

def nexttask(color, tasks, cur):
    for i in range(len(tasks)):
        if tasks[i][0] == color and i>cur: return i
    return -2

input = []
for line in stdin: input.append(rstrip(line,'\n'))
nTestCases = int(input.pop(0))

for line in input:
    tokens = line.split(' ')
    N = tokens[0]
    tokens = tokens[1:len(tokens)]
    tasks = []
    for i in range(0,int(N)):
        task = tokens[(2*i):(2*i)+2]
        task[1] = int(task[1])
        tasks.append(task)
    t = 0
    oi = 0
    ol = 1
    od = False
    bi = 0
    bl = 1
    bd = False
    dt = -1
    while dt<len(tasks)-1:
        oi = nexttask('O',tasks,dt)
        if oi == -2 and not od: od = True
        if not od:
            if tasks[oi][1] > ol: ol += 1
            elif tasks[oi][1] < ol: ol -= 1
            elif oi==dt+1: dt=oi
        bi = nexttask('B',tasks,dt)
        if bi == -2 and not bd: bd = True
        if not bd:
            if tasks[bi][1] > bl: bl += 1
            elif tasks[bi][1] < bl: bl -= 1
            elif bi==dt+1 and dt != oi: dt=bi
        t += 1
        if dt == oi: oi += 1
        if dt == bi: bi += 1
    stdout.write("Case #%s: "%line+str(t)+'\n')
