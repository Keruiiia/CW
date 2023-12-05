'''
A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .
'''

def special_number(number):
    return ('Special!!', 'NOT!!')[len({'6', '7', '8', '9'} & set(str(number))) > 0]
	
#smart_solution

def special_number(n):
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"