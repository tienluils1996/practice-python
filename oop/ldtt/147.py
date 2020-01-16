n = int(input("nhap n: "))
flag = 1
t = n
while (t != 0):
    dv = n % 10
    if (dv % 2 == 0):
        flag = 0
    t = t//10
if(flag == 1):
    print("toan so le")
else:
    print("co so chan")
