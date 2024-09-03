'''
Your task is to return an output string that translates an input string s by replacing each character
in s with a number representing the number of times that character occurs
in s and separating each number with the sep character(s).
'''

def multiples(s1,s2,s3):
    more_num = max(s1, s2)
    less_num = min(s1, s2)
    res = [num for num in range(more_num, s3, more_num) if num % less_num == 0]
    return res
			

