'''
Create a function that takes a number as an argument and returns a grade based on that number.

Score	Grade
Anything greater than 1 or less than 0.6	"F"
0.9 or greater	"A"
0.8 or greater	"B"
0.7 or greater	"C"
0.6 or greater	"D"
Examples:

grader(0)   should be "F"
grader(1.1) should be "F"
grader(0.9) should be "A"
grader(0.8) should be "B"
grader(0.7) should be "C"
grader(0.6) should be "D"'''

def grader(score):
    for limit, grade in [(0.9, "A"), (0.8, "B"), (0.7, "C"), (0.6, "D")]:
        if limit <= score <= 1:
            return grade
    return 'F'
	

def test_grader():
	assert grader(1.01) == "F"
	assert grader(1) == "A"
	assert grader(1.01) == "F"
	assert grader(0.2) == "F"
	assert grader(0.7) == "C"
	assert grader(0.8) == "B"
	print("All tests passed!")