import sys
t = int(input())

for i in range(t):
    n = int(input())
    arr = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(n)])
    temp = []
    
    for i in range(n):
        if arr[0][1] >= arr[i][1]:
            temp.append(arr[i])
    temp = sorted(temp, key= lambda x: x[1])
    cnt = 1
    com = temp[0][0]
    for i in temp:
        if com > i[0]:
            com = i[0]
            cnt +=1
            
    print(cnt)