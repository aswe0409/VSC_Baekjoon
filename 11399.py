n = int(input())

arr = sorted(list(map(int, input().split())))

ret = 0
temp = []
for i in range(len(arr)):
    ret+= arr[i]
    temp.append(ret)
    
print(sum(temp))