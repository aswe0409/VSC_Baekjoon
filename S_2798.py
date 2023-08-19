from itertools import combinations

n , m = map(int, input().split())
card = sorted(list(map(int,input().split())))

temp = []
for i in combinations(card, 3):
    if sum(i) <= m:
        temp.append(sum(i))
    else:
        continue

print(max(temp))