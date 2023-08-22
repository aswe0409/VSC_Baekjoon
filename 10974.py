from itertools import permutations

num = int(input())
arr = [i for i in range(1,num+1)]

for i in permutations(arr,num):
    print(*i, end='\n')