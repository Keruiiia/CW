'''
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]
'''

def solve(arr): 
    res = []
    for el in arr[::-1]:
        if el not in res:
            res.append(el)
    return res[::-1]
	
def solve(arr): 
    return list(dict.fromkeys(arr[::-1]))[::-1]