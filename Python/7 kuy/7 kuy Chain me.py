'''
The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800
'''
def chain(init_val, functions):
    if not functions:
        return init_val
    for f in functions:
        init_val = f(init_val)
    return init_val