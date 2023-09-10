'''
In this kata, you will be given an array. Each value represents a meeting room.
Your job? Find the first empty one and return its index
(N.B. There may be more than one empty room in some test cases).

'X' --> busy
'O' --> empty
If all rooms are busy, return "None available!"
'''

def meeting(rooms):
    return rooms.index("O") if "O" in rooms else 'None available!'
	
def test_meeting():	
    assert meeting(['X', 'O', 'X']) == 1
    assert meeting(['O','X','X','X','X']) == 0
    assert meeting(['X','X','O','X','X']) == 2
    assert meeting(['X']) == 'None available!'
	print("All tests passed!")
	
test_meeting()