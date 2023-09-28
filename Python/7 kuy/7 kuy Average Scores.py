'''
Create a function that returns the average of an array of numbers ("scores"),
rounded to the nearest whole number. You are not allowed to use
any loops (including for, for/in, while, and do/while loops).

The array will never be empty.'''


import numpy as np

def average(array):
    return round(np.mean(array))
	
	
def test_average():
	assert_equals(average([5, 78, 52, 900, 1]), 207)
	assert_equals(average([5, 25, 50, 75]), 39)
	assert_equals(average([2]), 2)
	assert_equals(average([1, 1, 1, 1, 9999]), 2001)
	print("All tests passed!")
	
test_average()