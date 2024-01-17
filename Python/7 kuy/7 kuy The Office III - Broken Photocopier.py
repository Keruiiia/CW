'''
The bloody photocopier is broken... Just as you were sneaking around the office to print off your favourite binary code!

Instead of copying the original, it reverses it: '1' becomes '0' and vice versa.

Given a string of binary, return the version the photocopier gives you as a string.
'''
def broken(inp):
    res = ''
    for char in inp:
        if char == '0':
            res += '1'
        else:
            res += '0'
    return res

#smart_solution

def broken(inp):
    """Replace each '0' with '1' and vice versa."""
    return inp.translate(str.maketrans("01", "10"))