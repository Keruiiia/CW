'''
Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list [3, 4, 3, 6] the function should return 10,
and for the list [1, 10, 3, 10, 10] the function should return 4
'''

from collections import Counter

def sum_no_duplicates(l):
    res = 0
    for k, v in Counter(l).items():
        if v == 1:
            res += k
    return res
			

