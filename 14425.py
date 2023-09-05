import sys

n, m = map(int, sys.stdin.readline().split())

s = set([sys.stdin.readline() for _ in range(n)])
cnt = 0

for i in range(m):
    test = sys.stdin.readline()
    if test in s:
        cnt += 1
        
print(cnt)