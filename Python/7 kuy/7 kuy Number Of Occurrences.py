'''
Write a function that returns the number of occurrences of an element in an array.

Examples
sample = [0, 1, 2, 2, 3]
number_of_occurrences(0, sample) == 1
number_of_occurrences(4, sample) == 0
number_of_occurrences(2, sample) == 2
number_of_occurrences(3, sample) == 1
'''
def number_of_occurrences(element, sample):
    return sample.count(element)
	
sample = [0, 1, 2, 2, 3]

	
def test_number_of_occurrences():
    assert number_of_occurrences(4, sample) == 0
    assert number_of_occurrences(2, sample) == 2
    assert number_of_occurrences(-1, sample) == 0
	print("All tests passed!")
	
test_number_of_occurrences()