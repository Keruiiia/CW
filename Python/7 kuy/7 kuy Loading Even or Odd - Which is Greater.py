'''
Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return Even is greater than Odd

If the sum of odd numbers is greater than the sum of even numbers return Odd is greater than Even

If the total of both even and odd numbers are identical return Even and Odd are the same
'''

def even_or_odd(s):
    even, odd = 0, 0
    for num in s:
        n = int(num)
        if n & 1:
            odd += n
        else:
            even += n
    if even > odd:
        return 'Even is greater than Odd'
    elif odd > even:
        return 'Odd is greater than Even'
    else:
        return 'Even and Odd are the same'
		
def even_or_odd(s):    
    even_minus_odd = sum([-x if x % 2 else x for x in map(int, s)])
    if even_minus_odd > 0:
        return "Even is greater than Odd"
    elif even_minus_odd < 0:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"