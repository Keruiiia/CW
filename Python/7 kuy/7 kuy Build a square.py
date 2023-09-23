'''
I will give you an integer. Give me back a shape that is as long and wide
as the integer. The integer will be a whole number between 1 and 50.

Example
n = 3, so I expect a 3x3 square back just like below as a string:

+++
+++
+++
'''

def generate_shape(n):
    s = ""
    for i in range(n):
        s += "+" * n + "\n"
    return s[:-1]


def test_generate_shape():
    assert generate_shape(3) == '+++\n+++\n+++'
    assert generate_shape(8) == '++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++\n++++++++'
    print("All tests passed!")


test_generate_shape()