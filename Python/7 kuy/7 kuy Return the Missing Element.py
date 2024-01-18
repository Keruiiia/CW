'''
Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive), and returns the missing element.

Examples:
[0, 5, 1, 3, 2, 9, 7, 6, 4] --> 8
[9, 2, 4, 5, 7, 0, 8, 6, 1] --> 3
'''

def get_missing_element(seq): 
    res = set(range(10)) - set(seq)
    return list(res)[0]
	

#smart_solution

def get_missing_element(seq): 
    return 45 - sum(seq)