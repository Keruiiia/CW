'''
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

tripleX("abraxxxas") → true
tripleX("xoxotrololololololoxxx") → false
tripleX("softX kitty, warm kitty, xxxxx") → true
tripleX("softx kitty, warm kitty, xxxxx") → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false
'''

def triple_x(s):
    try:
        return s.index('x') == s.index('xxx')
    except:
        return False
		

#smart solution

import re

def triple_x(s):
    return re.match('[^x]*xxx', s) is not None