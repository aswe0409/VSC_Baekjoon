import sys

k, n = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]

min_val = int(1)
max_val = max(arr)

while(min_val <= max_val):
    mid = (min_val + max_val) // 2
    cnt = int(0)
    
    for i in arr:
        cnt = cnt + (i // mid)
        
    if cnt >= n:
        min_val = mid + 1
        
    else:
        max_val = mid - 1
        
print(max_val)