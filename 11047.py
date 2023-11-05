n, k = map(int, input().split())

money = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0

for i in money:
    cnt += k // i
    k %= i
        
print(cnt)