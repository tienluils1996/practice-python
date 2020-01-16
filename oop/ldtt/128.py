a = int(input("nhap a: "))
b = int(input("nhap b: "))
if(a>b):
    temp = a
    a = b
    b = temp
print(a,b,sep="_")