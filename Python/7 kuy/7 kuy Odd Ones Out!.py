'''
Challenge: You are given a list of numbers. The numbers each repeat a certain number
of times. Remove all numbers that repeat an odd number of times while
keeping everything else the same.
'''
from collections import Counter

def odd_ones_out(numbers):
    d = Counter(numbers)
    res = [num for num in numbers if d[num] % 2 == 0]
    return res
			

