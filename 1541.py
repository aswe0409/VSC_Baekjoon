arr = input().split('-')

ret = 0
sub = 0
temp = arr[0].split('+')
for i in temp:
    ret += int(i)
    
for i in range(1, len(arr)):
    for j in arr[i].split('+'):
        sub += int(j)
        
print(ret-sub)