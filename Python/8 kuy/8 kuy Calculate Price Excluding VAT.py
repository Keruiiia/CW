'''
Write a function that calculates the original product price, without VAT.

Example
If a product price is 200.00 and VAT is 15%, then the final product price (with VAT) is: 200.00 + 15% = 230.00

Thus, if your function receives 230.00 as input, it should return 200.00

Notes:

VAT is always 15% for the purposes of this Kata.
Round the result to 2 decimal places.
If null value given then return -1
'''

def excluding_vat_price(price):
    try:
        return round(price / 1.15, 2)
    except TypeError:
        return -1
		
	
def test_excluding_vat_price():
	assert excluding_vat_price(230.00) == 200.00
	assert excluding_vat_price(123) == 106.96
	assert excluding_vat_price(777) == 675.65
	assert excluding_vat_price(460.00) == 400.00
	assert excluding_vat_price(None) == -1
	print("All tests passed!")
	
test_excluding_vat_price()