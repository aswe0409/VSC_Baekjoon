a1 = int(input())
a2 = int(input())
a3 = int(input())

sum = a1 + a2 + a3

if (sum == 180 and a1 == a2 and a2 == a3):
    print("Equilateral")
    
elif(sum == 180 and a1 == a2 or a2 == a3 or a3 == a1):
    print("Isosceles")
    
elif(sum == 180 and a1 != a2 and a2 != a3 and a3 != a1):
    print("Scalene")
    
else:
    print("Error")