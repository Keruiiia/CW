'''
Your task is to check wheter a given integer is a perfect power.
If it is a perfect power, return a pair m and k with mk = n as a proof.
Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

Note: For a perfect power, there might be several pairs.
For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However,
the tests take care of this, so if a number is a perfect power, return any pair that proves it.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None
'''

def isPP(n):
    for i in range(2, int(n**0.5) + 1):
        p = 2
        while (pow := i ** p) <= n:
            if pow == n:
                return [i, p]
            p += 1
    return None
	
