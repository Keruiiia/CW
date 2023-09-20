'''
Implement a function that returns the minimal and the maximal value of a list (in this order).
'''

def get_min_max(seq): 
    return (min(seq), max(seq))
	
def test_get_min_max():
    assert get_min_max([1]) == (1,1)
    assert get_min_max([1,2]) == (1,2)
    assert get_min_max([2,1]) == (1,2)
	print("All tests passed!")
	
test_get_min_max()