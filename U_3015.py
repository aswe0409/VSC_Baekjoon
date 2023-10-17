import sys

n = int(input())

arr = [int(sys.stdin.readline()) for _ in range(n)]

cnt = int(0)

for i in range(0, len(arr)-1):
    for j in range(i+1, len(arr)):
        if(arr[i] >= arr[j]):
            cnt += 1
        else:
            cnt+=1
            break

print(cnt)