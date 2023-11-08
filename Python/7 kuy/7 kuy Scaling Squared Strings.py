'''
You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.
'''

def scale(strng, k, v):
    if not strng:
        return ""
    lst = strng.split("\n")
    for i, word in enumerate(lst):
        s = ""
        for char in word:
            s += char * k
        lst[i] = s
    return "\n".join(["\n".join([word] * v) for word in lst])
	
	
# alternative solution

def scale(strng, k, n):
    words = strng.split()
    words_h = ("".join(char * k for char in word) for word in words) 
    return "\n".join("\n".join(word for _ in range(n)) for word in words_h)