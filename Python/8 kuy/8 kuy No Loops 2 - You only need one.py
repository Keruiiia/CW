'''
You will be given an array a and a value x. All you need to do is check
whether the provided array contains the value, without using a loop.

Array can contain numbers or strings. x can be either. Return true if
the array contains the value, false if not. With strings you will need to account for case.'''


def check(a, x): 
    return x in a
	
def test_check():
	assert check([66, 101], 66) == True
    assert check([80, 117, 115, 104, 45, 85, 112, 115], 45) == True
    assert check(['t', 'e', 's', 't'], 'e') == True
    assert check(['what', 'a', 'great', 'kata'], 'kat') == False
	print("All tests passed!")
	
test_check()