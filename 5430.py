import sys
from collections import deque
 
n = int(sys.stdin.readline())

for i in range(n):
    order = input()
    length = int(sys.stdin.readline())
    word = input().strip('[').strip(']').split(',')
    
    if order.count('D') > length:
        print('error')
    
    else:
        if length == 0:
            print('[]')
            break
        
        if order.count("R") % 2 == 1:
            word = list(map(int, word))
            word = sorted(word, reverse=True)
            
        for j in order:
            if j =='D':

                word = deque(word)
                word.popleft()   
        word = list(map(str, word))   
        ret = '[' + ','.join(word)+']' 
        print(ret)
        # print('[',end='')
        # print(','.join(word), end='')
        # print(']')