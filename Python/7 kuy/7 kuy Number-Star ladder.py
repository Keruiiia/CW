'''
Using n as a parameter in the function pattern, where n>0, complete the codes to get the pattern (take the help of examples):

Note: There is no newline in the end (after the pattern ends)

Examples
pattern(3) should return "1\n1*2\n1**3", e.g. the following:

1
1*2
1**3
pattern(10): should return the following:

1
1*2
1**3
1***4
1****5
1*****6
1******7
1*******8
1********9
1*********10
'''
def pattern(n):
    res = '1\n'
    for i in range(2, n+1):
        res += '1' + (i-1) * '*' + f'{i}' + '\n'
    return res[:-1]
	
#smart_solution

def pattern(n):
    return "\n1".join("*" * i + str(i + 1) for i in range(n))