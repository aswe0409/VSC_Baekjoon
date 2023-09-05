n = int(input())

x= []
y = []

ret1 = 0
ret2 = 0

for _ in range(n):
    a, b= map(int,input().split())
    x.append(a)
    y.append(b)
    
x.append(x[0])
y.append(y[0])

for i in range(n):
    ret1 = x[i]* y[i+1] + ret1
    ret2 = x[i+1] * y[i] + ret2
    
print(round(abs((ret1 - ret2) / 2), 1))