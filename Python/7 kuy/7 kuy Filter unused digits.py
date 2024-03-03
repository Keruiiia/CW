'''
Given a varying number of integer arguments, return the digits that are not present in any of them.

Example:

[12, 34, 56, 78]  =>  "09"
[2015, 8, 26]     =>  "3479"
Note: the digits in the resulting string should be sorted.
'''

def unused_digits(*numbers):
    s1, s2 = set(), set("0123456789")
    for num in numbers:
        s3 = set(str(num))
        s1.update(s3)
    return ''.join(sorted(s2 - s1))
	
# smart_solution

def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))