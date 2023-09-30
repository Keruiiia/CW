'''
Complete the function to create backronyms. Transform the given string (without spaces)
to a backronym, using the preloaded dictionary and return a string of words,
separated with a single space (but no trailing spaces).

The keys of the preloaded dictionary are uppercase letters A-Z and the values are predetermined words, for example:

dictionary["P"] == "perfect"
Examples
"dgm" ==> "disturbing gregarious mustache"

"lkj" ==> "literal klingon joke"
'''

#preloaded variable: "dictionary"

def make_backronym(acronym):
    return " ".join(dictionary[char.upper()] for char in acronym)
	
def test_make_backronym():
	assert make_backronym('adh') == 'awesome disturbing hippy','Output not as expected'
    assert make_backronym('lmnop') == 'literal mustache newtonian oscillating perfect'
	assert make_backronym('wyv') == 'weird yogic volcano','Output not as expected'
	print("All tests passed!")
	
test_make_backronym()