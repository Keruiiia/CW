'''
Enjoying your holiday, you head out on a scuba diving trip!

Disaster!! The boat has caught fire!!

You will be provided a string that lists many boat related items.
If any of these items are "Fire" you must spring into action.
Change any instance of "Fire" into "~~". Then return the string.
'''

def fire_fight(s):
    return s.replace("Fire", "~~")
	
	
def test_fire_fight():
	assert fire_fight("Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast") == "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast"
	assert fire_fight("Mast Deck Engine Water Fire") == "Mast Deck Engine Water ~~"
	print("All tests passed!")
	

test_fire_fight()