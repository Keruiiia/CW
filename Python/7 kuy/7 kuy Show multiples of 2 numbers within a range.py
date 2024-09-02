'''
Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd parameter.

Python, Javascript, Java, Ruby versions: return results in a list/array

NOTICE:

Do NOT worry about checking zeros or negative values.
To find out if 3rd parameter (the upper limit) is inclusive or not, check the tests, it differs in each translation
'''

def multiples(s1,s2,s3):
    more_num = max(s1, s2)
    less_num = min(s1, s2)
    res = [num for num in range(more_num, s3, more_num) if num % less_num == 0]
    return res
			

