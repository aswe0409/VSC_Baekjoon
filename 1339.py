import math
n = int(input())
ret = 0
num = [9,8,7,6,5,4,3,2,1,0]
num_dict = {}

word = [input() for _ in range(n)]

word.sort(key=len, reverse=True)
for i in word:
    lang = len(i)
    for idx, j in enumerate(i):
        if j in num_dict:
            num_dict[j] += pow(10, lang-1)
        else:
            num_dict[j] = pow(10, lang-1)
        lang -= 1
num_dict = sorted(num_dict.items(), key = lambda x: x[1], reverse=True)

for i in range(len(num_dict)):
    ret += num_dict[i][1]*num[i]
    
print(ret)