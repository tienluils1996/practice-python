# 01
def string_length(str1):
    ''' hàm trả về số kí tự trong chuỗi
    tương tự hàm len()
    '''
    count = 0
    for char in str1:
        count += 1
    return count
# print(string_length('w3resource.com'))

# 02
def char_frequency(str1):
    """ hàm trả về tần số ký tự trong 1 chuỗi 
    tương tự: from collections import Counter 
    """
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
# print(char_frequency('google.com'))

# 03
def string_both_ends(str):
    if len(str) < 2:
        return ''

    return str[0:2] + str[-2:]

# print(string_both_ends('w3resource'))
# print(string_both_ends('w3'))
# print(string_both_ends('w'))

# 04
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    
    return str1

# print(change_char('restart'))



