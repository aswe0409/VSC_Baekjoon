m = int(input())
n = int(input())

yaksu = []

for i in range(m, n+1):
    cnt = 0
    for j in range(1,i+1):
        if(i % j == 0):
            cnt +=1
    if cnt == 2:
        yaksu.append(i)

if len(yaksu) == 0:
    print(-1)
else:
    print(sum(yaksu))
    print(min(yaksu))