'''
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3'''

def highest_rank(arr):
    lst, d = set(arr), {}
    for num in lst:
        d[num] = arr.count(num)
    max_value = max(d.values())
    max_keys = [k for k, v in d.items() if v == max_value]
    max_key = max(max_keys)
    return max_key


def test_power_of_two():
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
    assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]) == 10
    print("All tests passed!")