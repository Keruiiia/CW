'''
Write a function called calculate that takes 3 values. The first and third values are numbers.
The second value is a character. If the character is "+" , "-", "*", or "/",
the function will return the result of the corresponding mathematical function
on the two numbers. If the string is not one of the specified characters,
the function should return null (throw an ArgumentException in C#).

calculate(2,"+", 4); //Should return 6
calculate(6,"-", 1.5); //Should return 4.5
calculate(-4,"*", 8); //Should return -32
calculate(49,"/", -7); //Should return -7
calculate(8,"m", 2); //Should return null
calculate(4,"/",0) //should return null
Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made,
return null (throw an ArgumentException in C#)/(None in Python).
'''

def calculate(num1, operation, num2): 
    d = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    try:
        return d[operation](num1, num2)
    except (ZeroDivisionError, KeyError):
        return None
		
def test_calculate():
    assert calculate(3.2,"+", 8) == 11.2
    assert calculate(3.2,"-", 8) == -4.8
    assert calculate(3.2,"/", 8) == 0.4
    assert calculate(3.2,"*", 8) == 25.6
	assert calculate(-3,"/", 0) == None
    assert calculate(-3,"w", 0) == None
	print("All tests passed!")
	
test_calculate()
