a , b = input().split()

gap = []
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            gap += 1
    print(gap)
    quit()
    
elif a in b:
    print(0)
    quit()
    
else:
    for i in range(len(b) - len(a)):
        pass