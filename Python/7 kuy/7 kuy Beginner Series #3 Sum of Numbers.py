'''
Given two integers a and b, which can be positive or negative, find the sum of all
the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
'''

def get_sum(a,b):
    s = 0
    if b > a:
        for x in range(a, b+1):
            s += x
        return s
    elif a > b:
        for x in range(b, a+1):
            s += x
        return s
    elif a == b:
        return a