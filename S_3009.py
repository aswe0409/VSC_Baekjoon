x = []
y = []

for _ in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

for i in x:
    if(x.count(i) == 1):
        x_ret = i
        
for i in y:
    if(y.count(i)== 1):
        y_ret = i
        
print(x_ret, y_ret)