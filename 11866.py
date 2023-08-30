from collections import deque

n, k = map(int,input().split())

people = deque([i for i in range(1,n+1)])
dead = []

while people:
    for i in range(k-1):
        people.append(people.popleft())
        
    dead.append(people.popleft())

print('<', end='')
for i in range(len(dead)-1):
    print(f"{dead[i]}, ", end='')
    
print(dead[-1],end='') 
print('>', end='')