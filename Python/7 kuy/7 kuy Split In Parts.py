'''
The aim of this kata is to split a given string into different strings of equal size (note size of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
Assumptions:

String length is always greater than 0
String has no spaces
Size is always positive'''

def split_in_parts(s, part_length): 
    new_s, num = "", part_length 
    for i, char in enumerate(s):
        if i % num == 0:
            new_s += f" {char}"
        else:
            new_s += char
    return new_s.strip()
	
# smart solution
def split_in_parts(s, n): 
    return ' '.join([s[i:i+n] for i in range(0, len(s), n)])
	
def test_split_in_parts():
	assert split_in_parts("supercalifragilisticexpialidocious", 3) == "sup erc ali fra gil ist ice xpi ali doc iou s"
    assert split_in_parts("HelloKata", 1) == "H e l l o K a t a"
	assert split_in_parts("HelloKata", 9) == "HelloKata"
	print("All tests passed!)
	
test_split_in_parts()