'''
The goal is to create a function of two inputs number and power,
that "raises" the number up to power (ie multiplies number by itself power times).

Examples
number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
number_to_pwr(10, 6) # -> 1000000
'''

def number_to_pwr(number, p): 
    res = 1
    for i in range(p):
        res *= number
    return res