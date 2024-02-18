'''
Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
'''

def consonant_count(s):
    return len([char for char in s.lower() if char in 'qwrtyplkjhgfdszxcvbnm'])
	
def consonant_count(str):
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")