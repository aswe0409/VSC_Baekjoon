n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key = lambda x: (x[1], x[0]))
cnt = 0
temp = 0
for i, j in arr:
    if temp == 0:
        temp = j
        cnt += 1
    elif i >= temp:
        temp = j
        cnt +=1
        
print(cnt)