'''
Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

The objective is to set each of the 26 characters of the output string to either '1' or '0' based on the fact
whether the Nth letter of the alphabet is present in the input (independent of its case).

So if an 'a' or an 'A' appears anywhere in the input string (any number of times),
set the first character of the output string to '1', otherwise to '0'. if 'b' or 'B' appears
in the string, set the second character to '1', and so on for the rest of the alphabet.
'''
def change(st):
    draft = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    st = st.lower()
    for char in draft:
        if char in st:
            res += '1'
        else:
            res += '0'
    return res
	
#smart_solution

from string import ascii_lowercase


def change(st):
    source = st.lower()
    return ''.join('1' if q in source else '0' for q in ascii_lowercase)