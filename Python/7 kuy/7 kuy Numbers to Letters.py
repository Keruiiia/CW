'''
Given an array of numbers (in string format), you must return a string.
The numbers correspond to the letters of the alphabet in reverse order:
a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid.
'''

def switcher(arr):
    letters = (chr(x) for x in range(97, 123))
    digits = (str(d) for d in range(26, 0, -1))
    d = {k: v for k, v in zip(digits, letters)}
    d["27"] = '!'
    d["28"] = '?'
    d["29"] = ' '
    return ''.join(d[x] for x in arr)
	

def test_switcher():
    assert switcher(['24', '12', '23', '22', '4', '26', '9', '8']) == 'codewars'
    assert switcher(['25','7','8','4','14','23','8','25','23','29','16','16','4']) == 'btswmdsbd kkw'
    assert switcher(['4', '24']) == 'wc'
    assert switcher(['12']) == 'o'
	print("All tests passed!")
	
	
test_switcher()