'''
Create a function that takes an integer argument of seconds and converts the value
into a string describing how many hours and minutes comprise that many seconds.

Any remaining seconds left over are ignored.

Note:
The string output needs to be in the specific form - "X hour(s) and X minute(s)"

For example:

3600 --> "1 hour(s) and 0 minute(s)"
3601 --> "1 hour(s) and 0 minute(s)"
3500 --> "0 hour(s) and 58 minute(s)"
323500 --> "89 hour(s) and 51 minute(s)"
'''

def to_time(seconds):
    hours = seconds // 3600
    mint = seconds % 3600 // 60
    return f"{hours} hour(s) and {mint} minute(s)"


def test_to_time():
    assert to_time(3600) == '1 hour(s) and 0 minute(s)'
    assert to_time(3601) == '1 hour(s) and 0 minute(s)'
    assert to_time(3500) == '0 hour(s) and 58 minute(s)'
    assert to_time(323500) == '89 hour(s) and 51 minute(s)'
    print("All tests passed!")

test_to_time()