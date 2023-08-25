import sys

room = int(input())
people = list(map(int, sys.stdin.readline().split()))
head_see, sub_see = map(int,input().split())

head = 0

for i in people:
    if i <= head_see:
        head += 1
         
    if i > head_see:
        head += 1
        i -= head_see
        if i % sub_see == 0:
            head = head + (i // sub_see)

        else:
            head= head +1 +(i // sub_see)
            
                   
print(head)                 