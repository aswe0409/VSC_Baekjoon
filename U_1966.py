from collections import deque
import sys

n = int(input())

for _ in range(n):
    leng , target = map(int, sys.stdin.readline().split())
    if leng == 1:
        print(1)
        
    else:
        for i in range(leng):
            arr = deque(map(int, sys.stdin.readline().split()))
            
            if arr[0] < arr[1]:
                