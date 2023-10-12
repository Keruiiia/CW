'''
Implement the function which should return true if given object is a vowel
(meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.
'''

import re
def is_vowel(s): 
    regex = r'^[aeiou]{1}$'
    return bool(re.match(regex, re.escape(s), re.IGNORECASE))