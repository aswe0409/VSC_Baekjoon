import sys
n = int(input())

now = list(map(int, sys.stdin.readline().split()))
cnt = 1
temp = []

while now:
    if cnt == now[0]:
        now.pop(0)
        cnt +=1
        
    else:
        temp.append(now.pop(0))
        
    while temp:
        if temp[-1] == cnt:
            temp.pop()
            cnt += 1
            
        else:
            break
if temp:
    print("Sad")
else:
    print("Nice")