'''
Create a function named rotate() that accepts a string argument and returns an array of strings with each letter from the input string being rotated to the end.

rotate(Hello)  = [elloH, lloHe, loHel, oHell, Hello]
Note The original string should be included in the output array.
The order matters. Each element of the output array should be the rotated version of the previous element.
The output array SHOULD be the same length as the input string. The function should return an empty array with a 0 length string, '', as input.
'''
def rotate(s):
    if not s:
        return []
    res = [s[1:] + s[0]]
    for _ in range(len(s) - 1):
        res.append(res[-1][1:] + res[-1][0])
    return res
	
def rotate(str_):
    return [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]