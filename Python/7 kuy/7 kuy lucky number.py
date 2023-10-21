'''
Write a function to find if a number is lucky or not.
If the sum of all digits is 0 or multiple of 9 then the number is lucky.

1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisible by 9, hence number is lucky.

Function will return true for lucky numbers and false for others.
'''

def is_lucky(n):
    if n == 0:
        return True
    s = 0
    while n > 0:
        ost = n % 10
        s += ost
        n //= 10
    return s % 9 == 0
	
# smart solution
def is_lucky(n):
    return n % 9 == 0

	
def test_is_lucky():
	assert is_lucky(1892376) == True
    assert is_lucky(189237) == False
    assert is_lucky(18922314324324234423437) == False
	print("All tests passed!")