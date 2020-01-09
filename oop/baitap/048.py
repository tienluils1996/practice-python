x = int(input("nhap x: "))
n = int(input("nhap n: "))
S = x
i = 1
while i <= n:
    S = S*(x +i)
    i = i+1
print(S)