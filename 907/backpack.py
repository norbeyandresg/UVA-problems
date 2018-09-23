#Explanation of the problem santiago rengifo
from sys import stdin

MAX = 610
sites = [ None for i in range(MAX) ]
sums,omin,omax,n,k = None,None,None,None,None

def solve():
  global sites,sums,omin,omax,n,k
  lo, hi = 0, sums
  while lo + 1 != hi:
    x = lo + ((hi-lo)>>1)
    temp1 , temp2, flag = x, k, 0
    if x >= omax:
      for q in sites[:n]:
        if temp1 >= q:
          temp1 -= q
        elif x >= q and temp2 > 0: 
          temp1 = x - q
          temp2 -= 1
        else:
          flag = -1
      if flag == 0:
        hi = x
      else:
        lo = x
    else:
      lo = x
  return hi

def main():
  global sites,sums,omin,omax,n,k
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    omin,omax,sums = float('inf'),float('-inf'),0
    for i in range(n):
      sites[i] = int(inp.readline().strip())
      if sites[i]>omax: omax = sites[i]
      if sites[i]<omin: omin = sites[i]
      sums += sites[i]
    if sums==0:
      print(0)
    else:
      print(solve())
    l = stdin.readline().strip()

main()
