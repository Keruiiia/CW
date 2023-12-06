'''
Count how often sign changes in array.

result
number from 0 to ... . Empty array returns 0

example
const arr = [1, -3, -4, 0, 5];

/*
| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |
*/

catchSignChange(arr) == 2;
'''

def catch_sign_change(lst):
    res = list(map(lambda el: 1 if el >= 0 else 0, lst))
    counter = 0
    for i in range(1, len(res)):
        if res[i] != res[i-1]:
            counter += 1
    return counter
	
#smart_solution

def catch_sign_change(lst):
    return sum( (x >= 0) != (y >= 0) for x, y in zip(lst, lst[1:]) )