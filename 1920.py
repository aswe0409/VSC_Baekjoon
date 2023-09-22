import sys

n = int(input())
a = sorted(list(map(int, sys.stdin.readline().split())))

m = int(input())
b = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    target = b[i]
    left = 0
    right = len(a) - 1
    while(left <= right):
        mid = left + (right - left) // 2
        
        if target == a[mid]:
            print(1)
            break
        elif target < a[mid]:
            right = mid - 1
            
        else:
            left = mid + 1
    else:
        print(0)
            