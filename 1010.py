from itertools import combinations

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    r = int(1)
    a= int(1)
    
    for i in range(n,0,-1):
        r = r * i
        
    for j in range(n):
        a = a * m
        m -= 1
        
    print(a//r)