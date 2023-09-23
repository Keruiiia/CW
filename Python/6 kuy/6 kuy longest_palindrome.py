'''
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0'''

def longest_palindrome(s):
    length = len(s)
    if length == 0:
        return 0
    longest = 1
    for i in range(length):
        for j in range(i + longest, length):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                longest = j - i + 1
    return longest


def test_logest_palindrome():
    assert longest_palindrome("baa") == 2
    assert longest_palindrome("aab") == 2
    assert longest_palindrome("abcdefghba") == 1
    assert longest_palindrome("baablkj12345432133d") == 9
    print("All tests passed!")


test_logest_palindrome()