'''
Complete the function to find the count of the most frequent item of an array.
You can assume that input is an array of integers. For an empty array return 0

Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.
'''

def most_frequent_item_count(collection):
    try:
        return max(collection.count(elem) for elem in set(collection))
    except ValueError:
        return 0
		

def test_most_frequent_item_count():
	assert most_frequent_item_count([3, -1, -1]) == 2
    assert most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]) == 5
    assert most_frequent_item_count([]) == 0
    assert most_frequent_item_count([9]) == 1
	print("All tests passed!")
	
test_most_frequent_item_count()