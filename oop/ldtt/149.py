x = int(input("nhap x: "))
y = int(input("nhap y: "))
a = abs(x)
b = abs(y)
while (a*b != 0):
    if(a > b):
        a = a-b
    else:
        b = b-a
print(a+b)
