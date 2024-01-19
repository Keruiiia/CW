'''
Write a function with the signature shown below:

def is_int_array(arr):
    return True
returns true  / True if every element in an array is an integer or a float with no decimals.
returns true  / True if array is empty.
returns false / False for every other input.
'''
def is_int_array(arr):
    if type(arr) != list:
        return False
    res = []
    for el in arr:
        if type(el) == int:
            res.append(True)
        elif type(el) == float:
            if str(el)[-1] == '0':
                res.append(True)
            else:
                res.append(False)
        else:
            res.append(False)
    return all(res)
	
#smart_solution

def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)