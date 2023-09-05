num = int(input())

people = [list(map(int,input().split())) for i in range(num)]

for i in range(num):
    cnt = 1
    for j in range(num):
        if(people[i][0] < people[j][0] and people[i][1] < people[j][1]):
            cnt +=1
    print(cnt,end= " ")
    
    
    
    