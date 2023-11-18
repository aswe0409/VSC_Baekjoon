import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())

    if x == 0:
        if len(arr) <= 0:
            print(0)

        else:
            temp = heapq.heappop(arr)
            print(temp*-1)
    else:
        heapq.heappush(arr, x * -1)