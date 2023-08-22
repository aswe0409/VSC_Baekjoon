n = int(input())

end = []
i = 0

while(True):
    if('666' in str(i)):
        end.append(i)
        i+=1
        
    else:
        i+=1
        
    if(len(end) == n):
        break
print(max(end))
