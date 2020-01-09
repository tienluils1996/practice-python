n  = int(input("nhap n: "))
S = 1
i = 1
while i <= n:
    S = S*(i + 1/i*i)
    i = i + 1
print(S)