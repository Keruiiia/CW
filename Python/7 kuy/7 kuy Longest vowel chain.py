'''
The vowel substrings in the word codewarriors are o,e,a,io.
The longest of these has a length of 2. Given a lowercase string that has alphabetic
characters only (both vowels and consonants) and no spaces,
return the length of the longest vowel substring. Vowels are any of aeiou.
'''

def solve(s):
    if not s:
        return 0
    st = ""
    for i, x in enumerate(s):
        if x in 'aeiou':
            st += x
        else:
            st += " "
    return len(max(st.split(), key=len))
	
#smart solution

import re
def solve(s):
  return len(max(re.findall(r"[aeiou]+", s), key=len, default=""))