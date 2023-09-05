import sys

n = int(sys.stdin.readline())
sang = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
idx = 0

for i in range(m):
    if card[i] in sang:
        print(1, end = ' ')
    else:
        print(0, end = ' ')