n = int(input("nhap n: "))
S = 0
i = 1
while i <= 2*n + 1:
    S = S + 1/i
    i = i + 2
print(S)