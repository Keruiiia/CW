'''
You are given a integer array formula. Array contains only digits 1-8 that represents
material 1-8. Your task is to determine if the formula is valid. Returns true if it's valid, false otherwise.

Example
For formula = [1,3,7], The output should be true.

For formula = [7,1,2,3], The output should be false.

For formula = [1,3,5,7], The output should be false.
'''

def isValid(formula):
    if ((not 7 in formula) and (not 8 in formula)):
        return False
    if ((1 in formula) and (2 in formula)):
        return False
    if ((3 in formula) and (4 in formula)):
        return False
    if ((5 in formula and not 6 in formula) or (6 in formula and not 5 in formula)):
        return False
    return True