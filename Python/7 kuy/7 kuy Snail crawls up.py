'''
The snail crawls up the column. During the day it crawls up some distance.
During the night she sleeps, so she slides down for some distance (less than crawls up during the day).

Your function takes three arguments:

The height of the column (meters)
The distance that the snail crawls during the day (meters)
The distance that the snail slides down during the night (meters)
Calculate number of day when the snail will reach the top of the column.
'''

def snail(column, day, night):
    days = 0
    while column > 0:
        column -= day
        if column <= 0:
            break
        column += night
        days += 1
    return days + 1
	
def snail(column, day, night):
    speed = day - night
    days = 1
    while column - day > 0:
        day += speed
        days += 1
    return days