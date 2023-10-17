n = int(input())

s = set()
ret = int(0)

for i in range(n):
    name = input()
    if name == 'ENTER':
        ret += len(s)
        s = set()
    else:
        s.add(name)
ret += len(s)
print(ret)