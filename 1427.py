n = input()
arr = []
for i in range(len(n)):
    arr.append(n[i])
    
arr = sorted(arr, reverse=True)
print(*arr, sep='')