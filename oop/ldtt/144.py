n = int(input("nhap n: "))
dem = 0
i = 1
while(i <= n):
    if (n % i == 0):
        dem = dem + 1
    i = i+1
if(dem == 2):
    print("NT")
else:
    print("khong NT")
