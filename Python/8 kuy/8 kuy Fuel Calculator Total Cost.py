'''
In this kata you will have to write a function that takes
litres and price_per_litre (in dollar) as arguments.

Purchases of 2 or more litres get a discount of 5 cents per litre,
purchases of 4 or more litres get a discount of 10 cents per litre,
and so on every two litres, up to a maximum discount of 25 cents per litre.
But total discount per litre cannot be more than 25 cents. Return the total
cost rounded to 2 decimal places. Also you can guess that there
will not be negative or non-numeric inputs.

Good Luck!

Note
1 Dollar = 100 Cents
'''

def fuel_price(litres, price_per_litre):
    discount_per_litre = min(0.25, (litres // 2) * 0.05)
    return round(litres * (price_per_litre - discount_per_litre), 2)