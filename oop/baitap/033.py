n = int(input("nhap n: "))
S = 0
i = 1
while i <= n:
    S = S + i/(i + 1)
    i = i + 1
print(S)