'''
Challenge: You are given a list of numbers. The numbers each repeat a certain number
of times. Remove all numbers that repeat an odd number of times while
keeping everything else the same.
'''

from collections import Counter

def sum_no_duplicates(l):
    res = 0
    for k, v in Counter(l).items():
        if v == 1:
            res += k
    return res
			

