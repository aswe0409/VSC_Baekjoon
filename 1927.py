import heapq
import sys

n = int(sys.stdin.readline())
heap = []


for i in range(n):
    num = int(sys.stdin.readline())
    
    if num >0:
        heapq.heappush(heap, num)
        
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))