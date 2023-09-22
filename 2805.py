import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


min_val = int(1)
max_val = max(tree)

while(min_val <= max_val):
    mid = (min_val + max_val) // 2
    leng = 0
    
    for i in tree:
        if i > mid:
            leng = leng + (i - mid)
            
    if leng < m:
        max_val = mid - 1
        
    else:
        min_val = mid + 1
        
print(max_val)