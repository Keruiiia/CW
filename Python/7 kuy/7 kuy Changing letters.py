'''
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.
'''

def swap(st):
    trans_table = str.maketrans("oiuea", "OIUEA")
    return st.translate(trans_table)
	
	
def test_swap():
	assert swap("HelloWorld!") ==  "HEllOWOrld!"
    assert swap("Sunday") == "SUndAy"
    assert swap("Codewars") == "COdEwArs"
    assert swap("Monday") == "MOndAy"
    assert swap("Friday") == "FrIdAy"
	print("All tests passed!")
	
test_swap()