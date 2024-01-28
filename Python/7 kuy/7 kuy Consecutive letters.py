'''
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.

For example: 
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True
All inputs will be lowercase letters.
'''

def solve(st):
    if len(st) == 1:
        return True
    al = 'abcdefghijklmnopqrstuvwxyz'
    st = ''.join(sorted(st))
    first, last = st[0], st[-1]
    ind_f, ind_l = al.index(first), al.index(last)
    return st == al[ind_f:ind_l + 1]
	
#smart_solution
