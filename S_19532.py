from itertools import product

a,b,c,d,e,f = map(int, input().split())

arr = [i for i in range(-999, 1000)]

for i in product(arr, repeat = 2):
    if((a * i[0]) + (b * i[1]) == c and (d * i[0]) + (e * i[1]) == f):
        print(i[0], i[1])
        quit()
    else:
        continue


# from itertools import permutations

# a,b,c,d,e,f = map(int, input().split())

# arr = [i for i in range(-999, 1000)]

# for i in permutations(arr,2):
#     if((a * i[0]) + (b * i[1]) == c and (d * i[0]) + (e * i[1]) == f):
#         print(i[0], i[1])
#         quit()
#     else:
#         continue

# 처음에 코드 짜고 제출 했을때 예제 입력 했을때 정답도 잘 나오고 아무리 생각해도 문제가 없는 코드인줄 알았는데
# i[0] i[1] 같은 값인 경우를 생각하지 못했다.
# i0,1에 같은 값이 들어갈수 있게 순열이 아닌 중복순열로 바꿔서 풀었다.