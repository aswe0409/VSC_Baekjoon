import sys

while True:
    length = sorted(list(map(int, sys.stdin.readline().split())))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        quit()
        
    else:
        if ((length[0] * length[0]) + (length[1]** 2)) == length[2] ** 2:
            print('right')
            
        else:
            print('wrong')