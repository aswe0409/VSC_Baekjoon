n , m = map(int,input().split())

board = [list(input()) for _ in range(n)]
ret = []

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for a in range(i,i+8):
            for b in range(j, j+8):
                if(a+b) % 2 == 0:
                    if(board[a][b] != 'W'):
                        white += 1
                    if(board[a][b] != 'B'):
                        black += 1
                        
                else:
                    if(board[a][b] !='B'):
                        white +=1
                    if(board[a][b] != 'W'):
                        black += 1
        ret.append(min(white,black))
        
print(min(ret))

# 경우의 수가 2가지 존재하는데
# I 처음시작이 흰색일 경우 II 처음 시작이 검정색일 경우 2가지 이다.
# 처음 시작이 흰색일 경우 짝수번 째 줄 짝수번 요소는 흰색이고
# 홀수번째줄 홀수번 요소는 흰색이다.
# 이 원리를 이용해 풀었고,

# 검정색일 경우와 흰색일 경우를 동시에 계산해 주어서 더 작은 값을 배열에 넣어주고 그 배열중에서 가장 작은 값을 뽑으면 최소 변경 횟수가 나온다.