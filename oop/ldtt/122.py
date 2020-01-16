k = int(input("nhap k: "))
at = 1
bt = 1
i = 2
while(i <= k):
    ahh = 3*bt+2*at
    bhh = at+3*bt
    i = i+1
    at = ahh
    bt = bhh

print(ahh)
print(bhh)
