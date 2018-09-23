#references: Javier Gomez
#https://github.com/ackoroa/UVa-Solutions/blob/master/UVa%201203%20-%20Argus/src/UVa%201203%20-%20Argus.cpp
from heapq import *
from sys import stdin

def solve(par):
    queries, k = par
    heap = []
    for q in queries:
        heappush(heap, [int(q[1]), int(q[0]), int(q[1])])
    results = []
    for i in range(int(k)):
        q = heappop(heap)
        results.append(q[1])
        q[0] += q[2]
        heappush(heap, q)
    return '\n'.join(str(e) for e in results)

  
    
  
def main():
    imp = stdin
    a = imp.readline().split()
    queries = []
    while (a != ["#"]):
        queries.append([(a[1]),(a[2])])
        a = imp.readline().split()
    numberExecutions = imp.readline().strip()
    valas = (queries,numberExecutions)
    print(solve(valas))    
main()
