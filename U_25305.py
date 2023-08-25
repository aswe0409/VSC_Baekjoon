num, people = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

print(arr[num - people])
