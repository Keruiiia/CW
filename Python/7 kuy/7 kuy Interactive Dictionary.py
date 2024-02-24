'''
In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana
Good luck and happy coding!
'''

class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        """ new_entry == PEP8 (forced by Codewars) """
        self.my_dict[key] = value