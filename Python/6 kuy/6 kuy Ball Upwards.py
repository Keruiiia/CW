'''
You throw a ball vertically upwards with an initial speed v (in km per hour).
The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t where
g is Earth's gravity (g ~ 9.81 m/s**2). A device is recording at every tenth
of second the height of the ball. For example with v = 15 km/h the device
gets something of the following form: (0, 0.0), (1, 0.367...),
(2, 0.637...), (3, 0.808...), (4, 0.881..) ... where the first number
is the time in tenth of second and the second number the height in meter.

Task
Write a function max_ball with parameter v (in km per hour) that returns
the time in tenth of second of the maximum height recorded by the device.

Examples:
max_ball(15) should return 4

max_ball(25) should return 7

Notes
Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary.
The maximum height recorded by the device is not necessarily the maximum height reached by the ball.
'''


def max_ball(v0):
    lst = [(0, 0.0)]
    v = v0 * 1000 / 3600
    for t in range(1, 1001):
        t *= 0.1
        lst.append((t * 10, v*t - 0.5*9.81*t*t))
    lst.sort(key=lambda tup: tup[1], reverse=True)
    return int(lst[0][0])
	
# smart solution
def max_ball(v0):
    return round(10*v0/9.81/3.6)
	
def test_max_ball():
	assert max_ball(37) == 10
    assert max_ball(45) == 13
    assert max_ball(99) == 28
    assert max_ball(85) == 24
	print("All tests passed!")
	
test_max_ball()