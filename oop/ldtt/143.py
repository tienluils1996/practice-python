n = int(input("nhap n: "))
S = 0
i = 1
while(i < n):
    if (n % i == 0):
        S = S+i
    i = i+1
if(S == n):
    print("HT")
else:
    print("khong HT")
