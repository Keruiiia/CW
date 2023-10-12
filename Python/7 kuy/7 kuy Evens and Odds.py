'''
This kata is about converting numbers to their binary or hexadecimal representation:

If a number is even, convert it to binary.
If a number is odd, convert it to hex.
Numbers will be positive. The hexadecimal string should be lowercased.
'''



def evens_and_odds(n):
    if not n & 1:
        return f"{n:b}"
    else:
        return f"{n:x}"