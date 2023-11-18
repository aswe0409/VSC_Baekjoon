import sys

s = sys.stdin.readline().rstrip()
q = int(input())

for i in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    temp = s[l:r+1]
    print(temp.count(a))