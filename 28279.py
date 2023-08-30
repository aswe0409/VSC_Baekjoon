from collections import deque
import sys

n = int(input())
dq = deque()

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    
    if a[0] == 1:
        dq.appendleft(a[1])
        
    elif a[0] == 2:
        dq.append(a[1])
        
    elif a[0] == 3:
        if len(dq) == 0:
            print(-1)
            
        else:
            print(dq.popleft())
            
    elif a[0] == 4:
        if len(dq) == 0:
            print(-1) 
        else:
            print(dq.pop())
            
    elif a[0] == 5:
        print(len(dq))
        
    elif a[0] ==6:
        if len(dq) == 0:
            print(1)
            
        else:
            print(0)
            
    elif a[0] == 7:
        if len(dq) == 0:
            print(-1)
            
        else:
            print(dq[0])
            
    elif a[0] == 8:
        if len(dq) == 0:
            print(-1)
            
        else:
            print(dq[-1])