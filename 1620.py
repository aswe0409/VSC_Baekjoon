import sys

n, m = map(int, sys.stdin.readline().split())

dogam = {}

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    dogam[i] = name
    dogam[name] = i
    
for _ in range(m):
    prob = sys.stdin.readline().rstrip()
    if prob.isdigit():
        print(dogam[int(prob)])
    else:
        print(dogam[prob])