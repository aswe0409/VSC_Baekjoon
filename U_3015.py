import sys
from collections import deque

n = int(input())

q = deque([int(sys.stdin.readline()) for _ in range(n)])

cnt = int(0)

for i in range(0, len(q)-1):
    for j in range(i+1, len(q)):
        if(q[i] >= q[j]):
            cnt += 1
        else:
            cnt+=1
            break

print(cnt)