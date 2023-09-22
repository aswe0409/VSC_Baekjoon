import sys
from collections import deque

n = int(input())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(input())
c = list(map(int, sys.stdin.readline().split()))

ret = deque()
for i in range(n):
    if a[i] == 0:
        ret.append(b[i])
        
for i in c:
    ret.appendleft(i)
    print(ret.pop(), end= ' ')