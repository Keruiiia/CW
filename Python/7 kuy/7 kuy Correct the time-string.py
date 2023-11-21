'''
A new task for you!

You have to create a method, that corrects a given time string.
There was a problem in addition, so many of the time strings are broken.
Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
Examples
"09:10:01" -> "09:10:01"  
"11:70:10" -> "12:10:10"  
"19:99:99" -> "20:40:39"  
"24:01:01" -> "00:01:01"  
If the input-string is null or empty return exactly this value! (empty string for C++) If the time-string-format is invalid, return null. (empty string for C++)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
'''

import re

def time_correct(s):
    if s is None:
        return None
    if s == '':
        return ''
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    if not re.match(pattern, s):
        return None
    h, m, s = [int(x) for x in s.split(':')]
    sum_sec = h*3600 + m*60 + s
    h, m, s = sum_sec // 3600 % 24, sum_sec % 3600 // 60, sum_sec % 60
    return ':'.join(str(i).zfill(2) for i in (h, m, s))
	
#smart_solution

def time_correct(t):
    if not t: return t
    try:
        h, m, s = map(int, t.split(':'))
        if s >= 60: s -= 60; m += 1
        if m >= 60: m -= 60; h += 1
        return '%02d:%02d:%02d' % (h % 24, m, s)
    except: pass