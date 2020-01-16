x = int(input("nhap x: "))
y = int(input("nhap y: "))
a = abs(x)
b = abs(y)
while (a*b != 0):
    if(a > b):
        a = a-b
    else:
        b = b-a
kq = abs(x*y)/(a+b)
print(kq)
