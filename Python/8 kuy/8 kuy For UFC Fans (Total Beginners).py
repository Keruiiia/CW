'''
If the winner is George Saint Pierre he will obviously say:

"I am not impressed by your performance."
If the winner is Conor McGregor he will most undoubtedly say:

"I'd like to take this chance to apologize.. To absolutely NOBODY!"
'''

def quote(fighter):
    k = fighter.lower()
    d = {'george saint pierre' : "I am not impressed by your performance.",
		'conor mcgregor': "I'd like to take this chance to apologize.. To absolutely NOBODY!"}
    return d[k]