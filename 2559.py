import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

psum = []
psum.append(sum(arr[:k]))

for i in range(n-k):
    psum.append(psum[i] - arr[i] + arr[k+i])

print(max(psum))