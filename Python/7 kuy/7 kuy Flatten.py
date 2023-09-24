'''
Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]
'''


def flatten(lst):
    res = []
    for i in lst:
      if isinstance(i, list):
        res.extend(i)
      else:
        res.append(i)
    return res
	
def test_flatten():
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]) == [1, 2, 3, "a", "b", "c", 1, 2, 3]
    assert flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"]) == [1, 2, 3, "a", "b", "c", 1, 2, 3, "a"]
    print("All tests passed!")

test_flatten()