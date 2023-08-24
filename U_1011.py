n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]


# for i in range(n):
#     cnt = 0
#     for j in range(arr[i][1] - arr[i][0]):
#         if arr[i][1]== arr[i][0] +1:
#             print(cnt)
#         else:
#             arr[i][0] += 1
#             cnt += 1

for i in range(n):
    for j in range(arr[i][1] - arr[i][0]):
        if arr[i][0] == 0:
            print(arr[i][1])
            break
            
        else:
            print(arr[i][1] - arr[i][0] -1)
            break