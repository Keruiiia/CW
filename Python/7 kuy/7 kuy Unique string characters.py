'''
In this Kata, you will be given two strings a and b and your task
will be to return the characters that are not common in the two strings.

For example:

solve("xyab","xzca") = "ybzc" 
--The first string has 'yb' which is not in the second string. 
--The second string has 'zc' which is not in the first string. 
Notice also that you return the characters from the first string concatenated with those from the second string.
'''

def solve(a,b):
    common = set(a) & set(b)
    return ''.join(char for char in a + b if char not in common)
	

def test_solve():
    assert solve("xyab","xzca") == "ybzc"
    assert solve("xyabb","xzca") == "ybbzc"
    assert solve("abcd","xyz") == "abcdxyz"
    assert solve("xxx","xzca") == "zca"
	print("All tests passed!")
	
test_solve()