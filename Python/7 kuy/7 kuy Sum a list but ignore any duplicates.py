'''
Please write a function that sums a list, but ignores any duplicated items in the list.

For instance, for the list [3, 4, 3, 6] the function should return 10,
and for the list [1, 10, 3, 10, 10] the function should return 4
'''

def freq_seq(s, sep):
    res, d = [], {}
    for char in s:
        d[char] = s.count(char)
        res.append(str(d[char]))
    return sep.join(res)
			

