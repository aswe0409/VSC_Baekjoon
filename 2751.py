num = int(input())

arr = [int(input()) for i in range(num)]

print(*sorted(arr), sep='\n')
