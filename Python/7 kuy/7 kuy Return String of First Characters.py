'''
In this exercise, a string is passed to a method and a new string has to be returned
with the first character of each word in the string.

For example:

"This Is A Test" ==> "TIAT"
Strings will only contain letters and spaces, with exactly 1 space between words, and no leading/trailing spaces.
'''
def make_string(s):
    res = s[0]
    for i, char in enumerate(s[1:], start=1):
        if s[i-1] == ' ':
            res += char
    return res