from collections import Counter
import sys
n = int(input())

arr = sorted([int(sys.stdin.readline()) for _ in range(n)])

print(round(sum(arr)/len(arr))) #산술평균
print(arr[len(arr) // 2]) #중앙값
# 최빈값
cnt = Counter(arr).most_common(2)

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

#범위 최대 최소 차이
print(max(arr) - min(arr))
