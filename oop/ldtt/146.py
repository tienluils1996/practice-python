n = int(input("nhap n: "))
dn = 0
t = n
while(t != 0):
    dv = t % 10
    dn = dn*10+dv
    t = t//10
if(dn == n):
    print("DX")
else:
    print("khong DX")
