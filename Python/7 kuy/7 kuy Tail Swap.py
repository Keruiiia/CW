'''
You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), but with the characters after each colon swapped.

Examples
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
'''

def tail_swap(strings):
    f, s = [], []
    for st in strings:
        first, second = st.split(':')
        f.append(first)
        s.append(second)
    return [':'.join([fe, se]) for fe, se in zip(f, s[::-1])]
	
#smart_solution

def tail_swap(strings):
    (h1, t1), (h2, t2) = (s.split(':') for s in strings)
    return [f"{h1}:{t2}", f"{h2}:{t1}"]