'''
Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. Assume that m is a positive integer.

Ex.

multiples(3, 5.0)
should return

[5.0, 10.0, 15.0]'''


def multiples(m, n):
    return [x*n for x in range(1, m+1)]

def test_multiples():
    assert multiples(3, 5) == [5, 10, 15]
    assert multiples(4, 3) == [3, 6, 9, 12]
    print("All tests passed")

test_multiples()