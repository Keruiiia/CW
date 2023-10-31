'''The autocomplete function will take in an input string and a dictionary
array and return the values from the dictionary that start with the input string.
If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.

Example:

autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
For this kata, the dictionary will always be a valid array of strings.
Please return all results in the order given in the dictionary, even if
they're not always alphabetical. The search should NOT be case sensitive,
but the case of the word should be preserved when it's returned.

For example, "Apple" and "airport" would both return for an input of 'a'.
However, they should return as "Apple" and "airport" in their original cases.

Important note:

Any input that is NOT a letter should be treated as if it is not there.
For example, an input of "$%^" should be treated as "" and an input of
"ab*&1cd" should be treated as "abcd".

(Thanks to wthit56 for the suggestion!)
'''

import re

def autocomplete(input_, dictionary):
    s = re.sub('[^a-zA-z]', '', input_).capitalize()
    len_sub, lst = len(s), []
    for word in dictionary:
        if word[:len_sub].capitalize() == s:
            lst.append(word)
    return lst[:5]
	