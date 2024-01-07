'''
arrayLeaders ({16, 17, 4, 3, 5, 2}) ==> return {17, 5, 2}
Explanation:
17 is greater than the sum all the elements to its right side

5 is greater than the sum all the elements to its right side

Note : The last element 2 is greater than the sum of its right elements (abstract zero)
'''
def array_leaders(numbers):
    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]