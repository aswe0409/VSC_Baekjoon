arr = sorted(list(map(int, input().split())))

if(arr[0] + arr[1] == arr[2]):
    print(arr[0] + arr[1] + arr[2] -1)
    
elif(arr[0] + arr[1] > arr[2]):
    print(arr[0] + arr[1] + arr[2])
    
elif(arr[0] + arr[1] < arr[2]):
    print((arr[0] + arr[1]) * 2 - 1)