'''
Find the last element of the given argument(s).

Examples
last([1, 2, 3, 4]) ==>  4
last("xyz")        ==> "z"
last(1, 2, 3, 4)   ==>  4
'''
def last(*args): 
    try:
        return args[-1][-1]
    except:
        return args[-1]