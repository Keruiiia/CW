'''
Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5
'''

def solution(n):
    part = n - int(n)
    if 0.25 <= part < 0.75:
        return int(n) + 0.5
    elif part >= 0.75:
        return int(n) + 1
    else:
        return int(n)
		
		
def solution(n):
    return round(2 * n) / 2