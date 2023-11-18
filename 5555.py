aim = input()
n = int(input())

cnt = 0

for i in range(n):
    ring = input()
    temp = ring * 2
    if aim in temp:
        cnt += 1
print(cnt)

