'''Complete the solution so that it returns a formatted string.
The return value should equal "Value is VALUE" where value is a 5 digit padded number.

Example:

solution(5)  # should return "Value is 00005"'''

def solution(value):
    return f'Value is {value:05d}'
	

def test_solution():
	assert solution(0) == 'Value is 00000'
    assert solution(5) =='Value is 00005'
    assert solution(109) == 'Value is 00109'
    assert solution(1204) == 'Value is 01204'
	print("All tests passed")