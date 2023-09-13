'''
In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

Examples:

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []
'''

def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]
	
''' Shitty-code

	def two_highest(arg1):
    try:
        max_1 = max(arg1)
        while max_1 in arg1:
            arg1.remove(max_1)
        if arg1:
            max_2 = max(arg1)
            return [max_1, max_2]
        return [max_1]
    except ValueError:
        return []
'''
def test_two_highest():
	assert two_highest([]) == []
    assert two_highest([15]) == [15]
    assert two_highest([15, 20, 20, 17]) == [20, 17]
	print("All tests passed!")
	
test_two_highest()