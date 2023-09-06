'''
The medians of a triangle are the segments that unit the vertices
with the midpoint of their opposite sides. The three medians of a
triangle intersect at the same point, called the barycenter or the
centroid. Given a triangle, defined by the cartesian coordinates of
its vertices we need to localize its barycenter or centroid.

The function bar_triang() or barTriang or bar-triang, receives the
coordinates of the three vertices A, B and C  as three different
arguments and outputs the coordinates of the barycenter O in an array [xO, yO]

This is how our asked function should work: the result of the
coordinates should be expressed up to four decimals, (rounded result).

You know that the coordinates of the barycenter are given by the following formulas.
'''

def bar_triang(pointA, pointB, pointC): 
    a = (pointA[0] + pointB[0] + pointC[0]) / 3.0
    b = (pointA[1] + pointB[1] + pointC[1]) / 3.0
    return [round(a, 4), round(b, 4)]
	
	
def test_bar_triang():
	assert bar_triang([4, 6], [12, 4], [10, 10]) == [8.6667, 6.6667]
    assert bar_triang([4, 2], [12, 2], [6, 10]) == [7.3333, 4.6667]
    assert bar_triang([4, 8], [8, 2], [16, 6]) == [9.3333, 5.3333])
    print("All tests passed!")
