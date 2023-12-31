'''
a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.

You may assume the input is always valid.

Examples
power_of_two(1024) ==> True
power_of_two(4096) ==> True
power_of_two(333)  ==> False
Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.
'''



def power_of_two(x):
    return x != 0 and ((x & (x - 1)) == 0)

def test_power_of_two():
    assert power_of_two(1024) is True
    assert power_of_two(4096) is True
    assert power_of_two(27) is False
    print("All tests passed!")


test_power_of_two()


'''
If `x` is a power of two, its binary representation will have only one bit set to 1,
and all other bits will be 0. For example, the number 8 is a power of two,
and its binary representation is `1000`. When we subtract 1 from `x`, we get a number
where all the bits that were 0 in `x` are now 1, and the bit that was 1 in `x` is now 0.
For example, `8 - 1` is `7`, and its binary representation is `0111`.

On the other hand, if `x` is not a power of two, its binary representation will have
more than one bit set to 1. For example, the number 6 is not a power of two,
and its binary representation is `0110`. When we subtract 1 from `x`, we get a number
where some bits are still set to 1. For example, `6 - 1` is `5`, and its binary representation is `0101`.

When we perform a bitwise AND operation between `x` and `x - 1`, we get a number where some
bits are still set to 1, because there are positions where both `x` and `x - 1` have a bit set to 1.
Therefore, `(x & (x - 1)) == 0` is `False`.'''