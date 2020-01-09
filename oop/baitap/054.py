n = int(input("nhap n: "))
S = 0
i = 2
while i <= n:
    if n%i ==0:
        S = S + i
    i = i+2
print(S)