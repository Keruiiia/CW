'''
dataand data1 are two strings with rainfall records of a few cities
for months from January to December. The records of towns are separated by \n.
The name of each town is followed by :.

data and towns can be seen in "Your Test Cases:".

Task:
function: mean(town, strng) should return the average of rainfall
for the city town and the strng data or data1 (In R and Julia this function is called avg).
function: variance(town, strng) should return the variance of
rainfall for the city town and the strng data or data1.
Examples:
mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)
'''

def mean(town, strng):
    towns = strng.split('\n')
    d = [x for x in towns if x.split(':')[0] == town]
    if d == []: return -1.0
    town, temps = d[0].split(':')
    temps = [float(x) for x in temps.replace(",", " ").split(" ") if not x.isalpha()]
    return sum(x for x in temps) / len(temps)


def variance(town, strng):
    if town not in strng: return -1.0
    towns = strng.split('\n')
    d = [x for x in towns if x.split(':')[0] == town]
    if d == []: return -1.0
    town, temps = d[0].split(':')
    temps = [float(x) for x in temps.replace(",", " ").split(" ") if not x.isalpha()]
    return np.var(temps)