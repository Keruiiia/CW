'''
Create a function that takes a string argument and returns that
same string with all vowels removed (vowels are "a", "e", "i", "o", "u").

Example (Input --> Output)

"drake" --> "drk"
"aeiou" --> ""
remove_vowels("drake") // => "drk"
remove_vowels("aeiou") // => ""
'''

def remove_vowels(strng):
    s = ""
    for char in strng:
        if char not in "aeiouAEIOU":
            s += char
    return s

# smart solution

REMOVE_VOWS = str.maketrans('','','aeiou')

def remove_vowels(s):
    return s.translate(REMOVE_VOWS)	
	
def test_remove_vowels():
	assert remove_vowels("drake") == "drk"
    assert remove_vowels("scholarstem") == "schlrstm"
    assert remove_vowels("codewars") == "cdwrs"
    assert remove_vowels("high fives!") == "hgh fvs!"
	print("All tests passed!")
	
test_remove_vowels()