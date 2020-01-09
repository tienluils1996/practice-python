# from lib import lib_list as l
from lib.lib_list import sum_list
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
# a = tuplex[:2] + tuplex[3:]
# print(a)
listx = list(tuplex)
listx.remove(5)
tuplex = tuple(listx)
print(tuplex)