'''
Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
Task
Your task is to return the correct string using the Template String Feature.
Input
Two Strings, no validation is needed.
Output
You must output a string containing the two strings with the word ```' are '```'''


def temple_strings(obj, feature): 
    return obj + " are " + feature
	
def test_temple_strings():
	assert temple_strings("Animals","Good") == 'Animals are Good'
    assert temple_strings("Animals","Good") == 'Animals are Good'
    assert temple_strings("You","Special") == 'You are Special'
    assert temple_strings("lives","frozen") == 'lives are frozen'
	print("All tests passed!")