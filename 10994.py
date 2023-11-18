n = int(input())

star = [[' ' for _ in range(n * 4 - 3)] for __ in range(n * 4 - 3)]

def fillStar(n, x, y):
    if n == 1:
        star[y][x] = '*'
        return

    length = n * 4 - 3

    for i in range(length):
        star[y+i][x] = '*'
        star[y + length - 1][x+i] = '*'
        star[y+i][x+length -1] = '*'
        star[y][x+i] = '*'

    fillStar(n-1, x+2 , y+2)


fillStar(n, 0, 0)

for i in star:
    print(''.join(i))