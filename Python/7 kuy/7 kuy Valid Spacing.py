'''
Your task is to write a function called valid_spacing() or validSpacing()
which checks if a string has valid spacing. The function should return
either true or false (or the corresponding value in each language).

For this kata, the definition of valid spacing is one space between words,
and no leading or trailing spaces. Words can be any consecutive sequence of
non space characters. Below are some examples of what the function should return:

* 'Hello world'   => true
* ' Hello world'  => false
* 'Hello world  ' => false
* 'Hello  world'  => false
* 'Hello'         => true
'''

def valid_spacing(s):
    if not s:
        return True
    counter_spaces = s.count(" ")
    counter_words = len(s.split()) - 1
    return counter_words == counter_spaces
	
def test_valid_spacing():
    assert valid_spacing('Hello world') == True
    assert valid_spacing(' Hello world') == False
    assert valid_spacing('Hello  world ') == False
    assert valid_spacing('Hello') == True
    assert valid_spacing('Helloworld') == True
	print("All tests passed!")
	
	
test_valid_spacing()