'''
Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all
consecutive but 6 is not, so that's the first non-consecutive number.
'''

def first_non_consecutive(arr):
    lst = list(range(arr[0], arr[-1] + 1))
    for x, y in zip(arr, lst):
        if x != y:
            return x
			
# smart solution

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]
			
			
