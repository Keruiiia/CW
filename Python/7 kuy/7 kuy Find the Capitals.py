'''
Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.

The method should return an array of sentences declaring the state or country and its capital.

Examples
[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
'''
def capital(capitals): 
    res = []
    for d in capitals:
        country, capital = d.values()
        res.append(f"The capital of {country} is {capital}")
    return res
	

def capital(capitals):
    return ["The capital of {} is {}".format(*x.values()) for x in capitals]