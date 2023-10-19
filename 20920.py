import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        arr.append(word)
        
# 단어장 원하는 조건으로 가공
cnt = Counter(arr)

ret = sorted(cnt.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in range(len(ret)):
    print(ret[i][0])