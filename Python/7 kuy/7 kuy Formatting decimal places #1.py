'''Each floating-point number should be formatted that only the first two
decimal places are returned. You don't need to check whether the input
is a valid number because only valid numbers are used in the tests.

Don't round the numbers! Just cut them after two decimal places!

Right examples:  
32.8493 is 32.84  
14.3286 is 14.32

Incorrect examples (e.g. if you round the numbers):  
32.8493 is 32.85  
14.3286 is 14.33
'''

def two_decimal_places(number):
    lst = str(number).split(".")
    lst[1] = lst[1][:2]
    return float(".".join(lst))

#smart solution 
def two_decimal_places(number):
    return int (number * 100) / 100.0