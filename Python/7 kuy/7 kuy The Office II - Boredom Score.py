'''
Every now and then people in the office moves teams or departments. Depending what
people are doing with their time they can become more or less boring. Time to assess the current team.

You will be provided with an object(staff) containing the staff names as keys, and the department they work in as values.

Each department has a different boredom assessment score, as follows:

accounts = 1
finance = 2
canteen = 10
regulation = 3
trading = 6
change = 6
IS = 8
retail = 5
cleaning = 4
pissing about = 25

Depending on the cumulative score of the team, return the appropriate sentiment:

<=80: 'kill me now'
< 100 & > 80: 'i can handle this'
100 or over: 'party time!!'
'''

def boredom(staff):
    d = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    res = 0
    for name, depatment in staff.items():
        res += d[depatment]
    if res <= 80:
        return 'kill me now'
    elif 80 < res < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
		
#smat_colution

boredom_scores = {
    'accounts': 1,
    'finance': 2 ,
    'canteen': 10 ,
    'regulation': 3 ,
    'trading': 6 ,
    'change': 6,
    'IS': 8,
    'retail': 5,
    'cleaning': 4,
    'pissing about': 25,
}

def boredom(staff):
    score = sum(map(boredom_scores.get, staff.values()))
    return (
        'kill me now' if score <= 80 else
        'i can handle this' if score < 100 else
        'party time!!'
    )