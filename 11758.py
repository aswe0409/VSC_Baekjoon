x,y = [], []
ret1, ret2 = 0, 0

for _ in range(3):
    a, b= map(int,input().split())
    x.append(a)
    y.append(b)
    
x.append(x[0])
y.append(y[0])

for i in range(3):
    ret1 = x[i] * y[i+1] + ret1
    ret2 = x[i+1] * y[i] + ret2
    
    
width = (ret1 - ret2) / 2

if width == 0:
    print(0)
    
elif width < 0:
    print(-1)
    
else:
    print(1)