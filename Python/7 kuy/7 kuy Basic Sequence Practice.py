'''In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".

[ 0,  1,    3,      6,   ...]
  0  0+1  0+1+2  0+1+2+3
Your Task
Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

Examples
 5  -->  [0,  1,  3,  6,  10,  15]
-5  -->  [0, -1, -3, -6, -10, -15]
 7  -->  [0,  1,  3,  6,  10,  15,  21,  28]'''
 
def sum_of_n(n):
   if n < 0:
       return [-sum(range(a)) for a in range(1, abs(n) + 2)]    
   return [sum(range(a)) for a in range(1, n + 2)]
	
def test_sum_of_n():
	assert sum_of_n(5) == [0, 1, 3, 6]
	assert sum_of_n(3) = [0, 1, 3, 6]
    assert sum_of_n(-4) ==[0, -1, -3, -6, -10]
    assert sum_of_n(1) == [0, 1]
	print("All tests passed")
	
test_sum_of_n()