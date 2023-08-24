from sys import stdin
input = stdin.readline
g = int(input())

ret = []
last = 1

for i in range(2, 100001):
    for j in range(last,i):
        if i*i - j*j == g:
            ret.append(i)
            last = j +1 
            break
        
        elif i * i - j * j < g:
            break
        
        elif i * i - j * j > g:
            last +=1

          
if(len(ret) == 0):
    print(-1)
else:
    print(*sorted(ret), sep ='\n')
    