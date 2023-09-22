'''
maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
Explanation:
Since the size (k) equal 3 , then the subsequence of size 3 whose gives product of maxima is  8 * 9 * 10 = 720
'''

def max_product(lst, n_largest_elements):
    res = 1
    lst = sorted(lst, reverse=True)[:n_largest_elements]
    for x in lst:
        res *= x
    return res
	
	
def test_max_product():
	assert max_product(list(range(10, -1, -1)), 5) == 10*9*8*7*6
    assert max_product([10,2,3,8,1,10,4], 5) == 9600
    assert max_product([13,12,-27,-302,25,37,133,155,-1], 5) == 247895375
	print("All tests passed!")

test_max_product()