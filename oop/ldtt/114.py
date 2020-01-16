n = int(input("nhap n:"))
at = -2
T = 3
P = 7
i = 2
while(i <= n):
    T = T*3
    P = P*7
    ahh = 5*at + 2*T - 6*P + 12
    i = i+1
    at = ahh
print(at)
