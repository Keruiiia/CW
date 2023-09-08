'''
Implement String#digit? (in Java StringUtils.isDigit(String)),
which should return true if given object is a digit (0-9), false otherwise.
'''

import re

def is_digit(n):
    return bool(re.match("\d\Z", n))
	
def test_is_digit():
	    assert is_digit("") == False
        assert is_digit("7") == True
        assert is_digit(" ") == False
        assert is_digit("a") == False
        assert is_digit("a5") == False
		print("All tests passed!")

test_is_digit()