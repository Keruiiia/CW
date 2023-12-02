'''
Kevin is noticing his space run out! Write a function that removes the spaces from the values
and returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space']
would produce ['i','ihave','ihaveno','ihavenospace']
'''

def spacey(array):
    start, res = '', []
    for word in array:
        start += word
        res.append(start)
    return res
	
#smart_solution

from itertools import accumulate

def spacey(a):
    return list(accumulate(a)) 