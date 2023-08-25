'''
Task
Given a number, Find if it is Jumping or not .


Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers.

Input >> Output Examples
jumpingNumber(9) ==> return "Jumping!!"
Explanation:
It's single-digit number'''

def jumping_number(number):
    number = str(number)
    for i, num in enumerate(number[:-1]):
        if int(number[i + 1]) not in range(int(num) - 1, int(num) + 2):
            return "Not"
    return "Jumping!!"


def test_multiples():
    assert jumping_number(4353456) == "Not"
    assert jumping_number(4343456) == "Jumping!!"
    assert jumping_number(98789876) == "Jumping!!"
    print("All tests passed")

test_multiples()