from collections import deque
import sys

n = int(input())

dq = deque()

for i in range(n):
    word = sys.stdin.readline().split()
    
    if word[0] == 'push':
        dq.append(word[1])
        
    elif word[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
            
    elif word[0] == 'size':
        print(len(dq))
        
    elif word[0] == 'empty':
        if len(dq) == 0:
            print(1)
            
        else:
            print(0)
            
    elif word[0] == 'front':
        if len(dq) == 0:
            print(-1)
            
        else:
            print(dq[0])
            
    elif word[0] == 'back':
        if len(dq) == 0:
            print(-1)
            
        else:
            print(dq[-1])