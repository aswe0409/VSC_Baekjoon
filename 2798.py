n , m = map(int, input().split())

card = sorted(list(map(int,input().split())))

ret = 300000

for i in range(0, n -2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = card[i]+ card[j] + card[k]
            
            if(m - temp >=0 and m - temp <= ret) :
                ret = m - temp
                
print(temp)
            

