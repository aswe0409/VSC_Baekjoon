n = int(input())

for i in range(n):
    arr = list(map(int,(str(i))))
    
    if(n - sum(arr) - i == 0):
        print(i)
        quit()

print(0)