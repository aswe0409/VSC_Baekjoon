num = int(input())
n = 2
while n !=1:
    if num == 1:
        break
    
    if num % n == 0:
        print(n)
        num = num // n
        
    else:
        n+=1