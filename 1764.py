import sys

n, m = map(int, sys.stdin.readline().split())

heard = set()
see = set()

for _ in range(n):
    heard.add(sys.stdin.readline().rstrip())
    
for __ in range(m):
    see.add(sys.stdin.readline().rstrip())
    
ret = sorted(heard & see)

print(len(ret))
print(*ret, sep='\n')