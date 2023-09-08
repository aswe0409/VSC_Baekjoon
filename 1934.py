n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ret = a * b

    while b > 0:
        a, b = b, a % b

    print(ret // b)