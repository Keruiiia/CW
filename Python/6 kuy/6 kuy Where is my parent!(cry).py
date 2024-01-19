'''
Mothers arranged a dance party for the children in school. At that party,
there are only mothers and their children. All are having great fun on the
dance floor when suddenly all the lights went out. It's a dark night and
no one can see each other. But you were flying nearby and you can see in
the dark and have ability to teleport people anywhere you want.

Legend:
-Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.
Task:
Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".
'''

def find_children(dancing_brigade):
    lst = []
    for char in dancing_brigade:
        ind = ord(char)
        if char.islower():
            ind -= 32
        lst.append((char, ind))
    lst.sort(key=lambda tup: (tup[1], tup[0]))
    return ''.join(tup[0] for tup in lst)
	
	
# smart solution
def find_children(s):
    return ''.join(sorted(s, key=lambda c: (c.lower(), c)))