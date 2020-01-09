import math
n  = int(input("nhap n: "))
S = 0
i = 1
while i <= n:
    S = S + math.sqrt(1+1/i*i+1/(i+1)**2)
    i = i + 1
print(S)