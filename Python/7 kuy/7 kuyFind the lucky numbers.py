'''
Write a function filterLucky/filter_lucky() that accepts a list of integers and filters the list to only include the elements that contain the digit 7.

For example,

ghci> filterLucky [1,2,3,4,5,6,7,68,69,70,15,17]
[7,70,17]
Don't worry about bad input, you will always receive a finite list of integers.
'''

def filter_lucky(lst):
    res = []
    for num in lst:
        if '7' in str(num):
            res.append(num)
    return res
	
def filter_lucky(lst):
    return list(filter(lambda k: '7' in str(k), lst))