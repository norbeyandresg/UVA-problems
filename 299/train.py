#source code https://goo.gl/1HTDlc
from sys import stdin

MAX = 25010
train = [ None for i in range(MAX) ]
memo = [ None for i in range(MAX) ]
swaps = 0

def merge(low, high):
  global swaps
  c = []
  i, j= 0, 0
  while i < len(low) and j< len(high):
    if low[i] < high[j]:
      c.append(low[i])
      i += 1
      swaps += j
    else:
      c.append(high[j])
      j += 1
  swaps += j*(len(low)-i)
  c+=low[i:]
  c+= high[j:]
  return c
  
def mergeSort(x):
  if len(x) == 1:
    return x
  mid = len(x)>>1
  low = mergeSort(x[:mid])
  high = mergeSort(x[mid:])
  return merge(low, high)
  
def solve(n):
  global train,memo
  x=train[:n]
  mergeSort(x)
  return swaps
  
def main():
  global train, swaps
  inp = stdin
  cases = int(inp.readline().strip())
  while cases>0:
    n = int(inp.readline().strip())
    tok = inp.readline().strip().split()
    for i in range(n): train[i] = int(tok[i])
    print('Optimal train swapping takes {0} swaps.'.format(solve(n)))
    cases -= 1
    swaps = 0
main()
