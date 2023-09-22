while True:
    num = input()
    if num == '0':
        quit()
        
    else:
        if num == num[::-1]:
            print('yes')
            
        else:
            print('no')