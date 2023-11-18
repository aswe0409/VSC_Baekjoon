import sys

m , n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

psum = [0]

for i in range(0, m):
    psum.append(psum[i] + arr[i])

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    print(psum[end]- psum[start-1])