'''
Count the number of exclamation marks and question marks, return the production.

Examples
""          --->   0
"!"         --->   0
"!ab? ?"    --->   2
"!!"        --->   0
"!??"       --->   2
"!???"      --->   3
"!!!??"     --->   6
"!!!???"    --->   9
"!???!!"    --->   9
"!????!!!?" --->  20
'''

def product(st):
    return st.count('!') * st.count('?')