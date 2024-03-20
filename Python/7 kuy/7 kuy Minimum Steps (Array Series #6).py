'''
Given an array of N integers, you have to find how many times you have to add up
the smallest numbers in the array until their Sum becomes greater or equal to K.
'''

def minimum_steps(numbers, value):
    return sum(sum(sorted(numbers)[:i+1]) < value for i in range(len(numbers)))