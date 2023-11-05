import sys

n = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
money = 0

if price[0] == min(price):
    money = price[0] * sum(distance)
    print(money)
    quit()
else:    
    money = distance[0] * price[0]

for i in range(1, n-1):
    if price[i-1] < price[i]:
        price[i] = price[i-1]
    money += distance[i] * price[i]
print(money)

