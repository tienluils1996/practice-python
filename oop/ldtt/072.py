n = int(input("nhap n:"))
S = 0
M = 0
i = 1
while(i < n):
    M = M + i
    S = S + 1/M
    i = i+1
print(S)
