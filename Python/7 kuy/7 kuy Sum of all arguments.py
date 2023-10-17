'''
Write a function that finds the sum of all its arguments.

eg:

sum_args(1, 2, 3) # => 6
sum_args(8, 2) # => 10
sum_args(1, 2, 3, 4, 5) # => 15
'''

def sum_args(*args):
    return sum(args)
	

def test_sum_args():
	assert  sum_args(1) == 1 
    assert  sum_args(1, 2) == 3
    assert  sum_args(5, 7, 9) == 21 
    assert  sum_args(12, 1, 1, 1, 1) == 16
	print("All tests passed!")
	
test_sum_args()