import sys

t = int(sys.stdin.readline())

for i in range(t):
    floor = int(sys.stdin.readline())
    ho = int(sys.stdin.readline())
    
    house = [x for x in range(1, ho+1)]
    
    for j in range(floor):
        for k in range(1 , ho):
            house[k] += house[k-1]
            
    print(house[-1])