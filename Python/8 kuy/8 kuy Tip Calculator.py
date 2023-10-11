'''
Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Python

Because you're a nice person, you always round up the tip, regardless of the service.
'''

from math import ceil

def calculate_tip(amount, rating):
    d = {
        "Terrible": 0,
        "Poor": 0.05,
        "Good": 0.1,
        "Great": 0.15,
        "Excellent": 0.2
    }
    try:
        return ceil(amount * d[rating.capitalize()])
    except:
        return 'Rating not recognised'
		
		
def test_calculate_tip():
	assert calculate_tip(30, "poor") == 2
    assert calculate_tip(20, "Excellent") == 4
    assert calculate_tip(20, "hi") == 'Rating not recognised'
    assert calculate_tip(107.65, "GReat") == 17
	print("All tests passed!")
	
	
test_calculate_tip()