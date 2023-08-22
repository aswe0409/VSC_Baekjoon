while True:
    arr = []
    a1, a2, a3 = map(int,input().split())
    arr.append(a1)
    arr.append(a2)
    arr.append(a3)
    
    arr.sort()
    
    if (a1 == 0 and a2 == 0 and a3 == 0):
        break
    
    elif (arr[0] + arr[1] > arr[2] and a1 == a2 and a2 == a3):
        print("Equilateral")
        
    elif(arr[0] + arr[1] > arr[2] and a1 == a2 or a2 == a3 or a3 == a1):
        print("Isosceles")
        
    elif(arr[0] + arr[1] > arr[2] and a1 != a2 and a2 != a3 and a3 != a1):
        print("Scalene")
        
    else:
        print("Invalid")