'''
Write a program that outputs the top n elements from a list.

Example:

largest(2, [7,6,5,4,3,2,1])
# => [6,7]'''

def largest(n, xs):
    if n:
        return sorted(xs)[-n:]
    return []
	
def test_largest():
	assert largest(2, [10,9,8,7,6,5,4,3,2,1] == [9,10])
    assert largest(3, [5,1,5,2,3,1,2,3,5]) == [5,5,5]
    assert largest(7, [9,1,50,22,3,13,2,63,5]) == [3, 5, 9, 13, 22, 50, 63]
	print("All tests passed!")
	

test_largest()