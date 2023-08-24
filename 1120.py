a , b = input().split()

gap = []

for i in range(len(b) - len(a)+1):
    cnt = 0
    temp = b[i:len(a)+i]
    for j in range(len(a)):
        if temp[j] != a[j]:
            cnt += 1
    gap.append(cnt)
    
print(min(gap))