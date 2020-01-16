def checkYear(n):
    if(n % 400 == 0):
        return True
    if(n % 4 == 0 and n % 100 != 0):
        return True
    return False
year = 1998
if(checkYear(year)):
    print("nam {0} la nam nhuan".format(year))
else:
    print("nam {0} khong phai la nam nhuan".format(year))
