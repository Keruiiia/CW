'''
Bob is a lazy man.

He needs you to create a method that can determine how many letters (both uppercase and lowercase ASCII letters) and digits are in a given string.

Example:

"hel2!lo" --> 6

"wicked .. !" --> 6

"!?..A" --> 1
'''

def count_letters_and_digits(s):
    res = 0
    for char in s:
        if char.isalpha() or char.isdigit():
            res += 1
    return res
	
#smart_solution

def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))