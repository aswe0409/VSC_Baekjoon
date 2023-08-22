while True:
    num = int(input())
    if num == -1:
        break
    else:
        yaksu = []

        for i in range(1,num):
            if(num % i == 0):
                yaksu.append(i)
                
        if(sum(yaksu)) == num:
            print(num, " = ", " + ".join(str(i) for i in yaksu), sep="")
            
        else:
            print(num, 'is NOT perfect.')