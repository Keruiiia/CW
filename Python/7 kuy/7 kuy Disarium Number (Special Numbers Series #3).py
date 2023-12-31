'''
Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.
disariumNumber(89) ==> return "Disarium !!"
Explanation:
Since , 81 + 92 = 89 , thus output is "Disarium !!"
disariumNumber(564) ==> return "Not !!"
Explanation:
Since , 51 + 62 + 43 = 105 != 564 , thus output is "Not !!"
'''

def disarium_number(n):
    res = enumerate(map(int, list(str(n))), 1)
    r = 0
    for i, num in res:
        r += num ** i
    return ('Not !!', 'Disarium !!')[r == n]