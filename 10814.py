import sys

n = int(input())

arr = []
for i in range(1, n+1):
    age, name = sys.stdin.readline().split()
    arr.append([int(age),i,name])
    
arr.sort()

for a,b,c in arr:
    print(f"{a} {c}")
    
    