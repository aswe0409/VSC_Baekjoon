n = int(input())

a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))

ret = 0

for i in a:
    ret += i* max(b)
    b.remove(max(b))
    
print(ret)    

