# 01
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
# print(sum_list([1,2,-8]))

# 02


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
# print(multiply_list([1,2,-8]))

# 03


def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
# print(max_num_in_list([1, 2, -8, 0]))

# 04


def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min
# print(smallest_num_in_list([1, 2, -8, 0]))

# 05


def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr
# print(match_words(['abc', 'xyz', 'aba', '1221']))

#06


def last(n): return n[-1]


def sort_list_last(tuples):
  return sorted(tuples, key=last)

# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 07
# a = [10,20,30,20,10,50,60,40,80,50,40]

# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)
# print(type(dup_items))
# print(uniq_items)
# print(type(uniq_items))
