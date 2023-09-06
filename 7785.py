import sys

n = int(input())
log = {}

for _ in range(n):
    name, state = sys.stdin.readline().split()
    
    if state == 'enter':
        log[name] = state
        
    else:
        del log[name]
        
sorted_log = sorted(log, reverse = True)
print(*sorted_log, sep='\n')