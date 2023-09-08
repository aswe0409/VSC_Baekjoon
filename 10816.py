import sys
from collections import Counter

n = sys.stdin.readline()
sang = list(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))

counter = Counter(sang)

for i in card:
    print(counter[i], end=' ')