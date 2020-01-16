n = int(input("nhap n:"))
x = int(input("nhap x:"))
S = 0
T = 1
M = 0
i = 1
while(i <= n):
    T = T*x
    M = M + i
    S = s + T/M
    i = i+1
print(S)
