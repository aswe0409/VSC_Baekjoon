from collections import deque
import sys

n = int(input())

q = deque(map(int, sys.stdin.readline().split()))
arr = deque()
for i, val in enumerate(q):
    arr.append((i+1,val))
    
temp = []

for i in range(n):
     temp.append(arr[0][0])
     a = arr[0][1]
     arr.popleft()
     if len(arr) <= 0:
         break
     
     if a > 0:
        for j in range(a - 1):
            arr.append(arr.popleft())
            
        
     elif a < 0:
        for j in range(a * -1):
            arr.appendleft(arr.pop())

print(*temp, end=' ')