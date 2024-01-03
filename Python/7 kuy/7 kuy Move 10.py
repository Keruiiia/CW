'''
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.
'''
def move_ten(st):
    res = ''
    for char in st:
        n = (ord(char) + 10)
        if n > 122:
            n = n  % 122 + 96
        res += chr(n)
    return res
	
A = 'abcdefghijklmnopqrstuvwxyz'

def move_ten(s):
    return ''.join(s.translate(str.maketrans(A, A[10:] + A[:10])))