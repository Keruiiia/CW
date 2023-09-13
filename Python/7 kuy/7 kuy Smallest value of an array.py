'''
Write a function that can return the smallest value of an array or the index of that value.
The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates.
Assume the second parameter will be a string holding one of two values: 'value' and 'index'.
'''
def find_smallest(numbers,to_return):
    if to_return == 'index':
        return numbers.index(min(numbers))
    return min(numbers)
	
def test_find_smallest():
	assert find_smallest([5,4,3,2,1],"value") == 1
	assert find_smallest([5,4,3,2,1],"index") == 4
	assert find_smallest([ 8, 0, 9],"index") == 1
	assert find_smallest([ 8, 0, 9],"value") == 0
	print("All tests passed!")
	
test_find_smallest()