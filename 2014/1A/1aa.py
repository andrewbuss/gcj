from sys import stdin, stdout

lines = stdin.read().re place('\r', '').split('\n')

T = int(lines.pop(0))

es = 0

def itoi(x):
    return int(''.join(map(str, x)), 2)


for CN in range(1, T + 1):
    es = 0
    N, L = lines.pop(0).split(' ')
    N = int(N)
    L = int(L)
    outlets = [map(int, x) for x in lines.pop(0).split(' ')]
    devices = [map(int, x) for x in lines.pop(0).split(' ')]

    d_ones = [0 for _ in range(L)]
    o_ones = [0 for _ in range(L)]
    o_comp = [0 for _ in range(L)]
    for device in devices:
        for i, digit in enumerate(device):
            if digit:
                d_ones[i] += 1
    for outlet in outlets:
        for i, digit in enumerate(outlet):
            if digit:
                o_ones[i] += 1
            else:
                o_comp[i] += 1
    # print "Outlets:", outlets
    # print "Devices:", devices
    # print o_ones
    # print o_comp
    # print d_ones
    switches = 0
    skips = []
    for i, dsum in enumerate(d_ones):
        if o_ones[i] == o_comp[i]:
            skips.append(i)
        elif dsum == o_ones[i]:
            pass
        elif dsum == o_comp[i]:
            # print "Switching", i
            for outlet in outlets: outlet[i] ^= 1
            switches += 1
        else:
            switches = 99999
            break
    stdout.write("Case #" + str(CN) + ': ')
    for i in range(L):
        for j in range(N):
            if outlets[]

    if switches > 10000 or not leq(outlets, ):
        stdout.write("NOT POSSIBLE\n")
    else:
        stdout.write(str(switches + es) + '\n')
