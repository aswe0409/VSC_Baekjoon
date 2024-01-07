n = int(input())

ret = 0

while n > 0:
    if n % 5 == 0:
        ret += n // 5
        print(ret)
        quit()

    else:
        ret += 1
        n -= 2

if n == 0:
    print(ret)

else:
    print(-1)