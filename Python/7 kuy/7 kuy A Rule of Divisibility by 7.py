'''
Your task is to return to the function seven(m) (m integer >= 0) an array (or a pair, depending on the language) of numbers, the first being the last number m with at most 2 digits obtained by your function (this last m will be divisible or not by 7), the second one being the number of steps to get the result.

Forth Note:
Return on the stack number-of-steps, last-number-m-with-at-most-2-digits 

Examples:
seven(371) should return [35, 1]
seven(1603) should return [7, 2]
seven(477557101) should return [28, 7]
'''

def seven(m):
    steps = 0
    while m > 99:
        q, r = divmod(m, 10)
        m = q - (2 * r)
        steps += 1
    return m, steps