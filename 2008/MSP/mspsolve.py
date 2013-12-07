from itertools import permutations

def scalar_product(a, b):
    total = 0
    for i in range(len(a)): total += a[i]*b[i]
    return total

def solve(n, v1, v2):
    return min([scalar_product(v1, v2n) for v2n in permutations(v2)])