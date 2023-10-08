'''Write a function that reverses the bits in an integer.

For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative.
'''

def reverse_bits(n):
    return int(''.join(reversed(bin(n)[2:])), 2)
	
# smart solution

def reverse_bits(n):
    return int(bin(n)[:1:-1],2)
	
	
def test_reverse_bits():
	assert reverse_bits(417) == 267
    assert reverse_bits(267) == 417
    assert reverse_bits(0) == 0
    assert reverse_bits(2017) == 1087
	print("All tests passed!")
	
	
test_reverse_bits()