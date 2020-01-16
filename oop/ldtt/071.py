n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = x
T = x
i = 3
while(i <= 2*n + 1):
    T = T * x * x
    S = S + T
    i = i+2
print(S)
