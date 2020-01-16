n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 0
T = 1
i = 2
while(i <= 2*n):
    T = T * x * x
    S = S + T
    i = i+2
print(S)
