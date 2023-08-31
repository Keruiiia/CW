'''
Write a function

vowel_2_index
that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string.
E.g:

vowel_2_index('this is my string') == 'th3s 6s my str15ng'
vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel_2_index('') == '' '''

def vowel_2_index(st):
    new_str = ''
    for i, char in enumerate(st):
        if char in ('aeiouAEIOU'):
            new_str += str(i+1)
            continue
        new_str += char
    return new_str