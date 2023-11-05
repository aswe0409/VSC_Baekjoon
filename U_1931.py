n = int(input())

arr = sorted([list(map(int, input().split())) for _ in range(n)])

cnt = 1
temp = arr[0][1]
for i,j in arr:
    if i >=temp:
        cnt +=1
        temp = j
        
print(cnt)