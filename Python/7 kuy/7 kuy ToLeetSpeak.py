'''
Your task is to write a function toLeetSpeak that converts a regular english sentence to Leetspeak.

More about LeetSpeak You can read at wiki -> https://en.wikipedia.org/wiki/Leet

Consider only uppercase letters (no lowercase letters, no numbers) and spaces.

For example:

toLeetSpeak("LEET") returns "1337"'''

def to_leet_speak(str):
    return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))
	
def test_to_leet_speak():
    assert to_leet_speak("LEET") == "1337"
    assert to_leet_speak("CODEWARS") == "(0D3W@R$"
    assert to_leet_speak("HELLO WORLD") == "#3110 W0R1D"	
	print("All tests passed!")