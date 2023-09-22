import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ja = a[0] * b[1] + b[0] * a[1]
mo = a[1] * b[1]


min_yaksu = math.gcd(ja, mo)
ja = ja // min_yaksu
mo = mo // min_yaksu

print(f"{ja} {mo}") 