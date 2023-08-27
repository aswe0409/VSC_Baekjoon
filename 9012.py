n = int(input())

for i in range(n):    
    vps = input()
    stack = []
    for j in vps:
        if j == '(':
            stack.append(j)
            
        elif j == ')':
            if stack:
                stack.pop()
                
            else:
                print("NO")
                break
            
    else: #break가 실행되면 이 부분은 실행 안 됨
        if stack:
            print("NO")
            
        else:
            print("YES")
        

# 처음에 생각한건 오른쪽 괄호랑 왼쪽 괄호의 갯수만 비교해서 동일하면 yes 출력을 하게 끔 코드를 잤는데 
# ))((  이렇게 들어온 경우는 개수는 동일 하지만 참이 아니라 수정 했다.
    
    