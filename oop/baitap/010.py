import math
x1 = int(input("nhap x1: "))
y1 = int(input("nhap y1: "))
x2 = int(input("nhap x2: "))
y2 = int(input("nhap y2: "))
x3 = int(input("nhap x3: "))
y3 = int(input("nhap y3: "))

a = math.sqrt((x2-x1)**2+(y2-y1)**2)
b = math.sqrt((x3-x2)**2+(y3-y2)**2)
c = math.sqrt((x3-x1)**2+(y3-y1)**2)

P  = a + b + c
print("chu vi hinh tam giac: ",  P)