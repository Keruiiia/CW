'''
The string given to your function has had an "egg" inserted directly after each consonant. You need to return the string before it became eggcoded.

Example
unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
//             "B---eg---in---n---er---"
Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.
'''

def unscramble_eggs(word):
    word = word.replace("egg", "")
    return word