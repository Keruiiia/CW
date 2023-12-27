'''
Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

Heron's formula:

(s∗(s−a)∗(s−b)∗(s−c))**0.5
​

Output should have 2 digits precision.
'''

def heron(a, b, c):
    s = (a + b + c) / 2
    res = round((s*(s-a)*(s-b)*(s-c))**0.5, 2)
    return res