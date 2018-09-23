#reference: class
from sys import stdin
INF = float('inf')
A = []

def solve(L,n,m):
    global A
    m = [0] + m + [L]
    A = {}
    return solv(0, len(m) - 1, m)
    
def solv(l,r,m):
    global A
    if (l,r) in A: return A[(l,r)]
    elif l == r-1: return 0
    mCost = INF
    for cut in range(l+1,r):
        cost = solv(l,cut,m) + solv(cut,r,m)
        mCost = min(cost,mCost)
    mCost = mCost + m[r] - m[l]
    A[(l,r)] = mCost
    return mCost
    
def main():
    global A
    inp = stdin
    L = int(inp.readline().strip())
    while L != 0:
        n = int(inp.readline().strip())
        A=list(map(int,inp.readline().strip().split()))
        print('The minimum cutting is {0}.' .format(solve(L,n,A)))
        L = int(inp.readline().strip())

main()