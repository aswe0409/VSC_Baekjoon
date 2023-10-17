n = int(input())

arr = [input() for _ in range(n)]
arr = set(arr)
arr = sorted(list(arr))
arr.sort(key = len)

print(*arr,sep='\n')
