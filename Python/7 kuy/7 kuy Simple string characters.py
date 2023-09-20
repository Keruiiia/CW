'''
In this Kata, you will be given a string and your task will be to return a
list of ints detailing the count of uppercase letters, lowercase,
numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.
'''

import re

def solve(s):
    return [len(re.findall(i,s)) for i in ('[A-Z]','[a-z]','\d','[^a-zA-Z0-9]')]


def test_solve():
	assert solve("Codewars@codewars123.com") == [1,18,3,2]
	assert solve("bgA5<1d-tOwUZTS8yQ") == [7,6,3,2]
	assert solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H") == [9,9,6,9]
	print("All tests passed!")
	
test_solve()