'''
Create a function called one that accepts two params:

a sequence
a function
and returns true only if the function in the params returns true for exactly one (1) item in the sequence.
'''

def one(sq, fun): 
    return sum(map(fun, sq)) == 1