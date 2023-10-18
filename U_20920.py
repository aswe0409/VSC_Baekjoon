import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
arr = []
ret = []
temp = []


for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) >= m:
        arr.append(word)
        
# 단어장 원하는 조건으로 가공
cnt = Counter(arr)

for i in range(0, len(cnt)-1):
    for j in range(i+1, len(cnt)):
        if cnt[i][1] == cnt[j][1]: #단어의 갯수가 같은 경우
            if len(cnt[i][0]) == len(cnt[j][0]): #단어의 갯수도 같고 길이도 길경우
                temp.append(cnt[i][0])
                temp.append(cnt[j][0])
                sorted(temp)
                ret.append(temp[0])
                ret.append(temp[1])
                pass
        else: #단어의 길이가 다른경우
            ret.append(cnt[i][0])
