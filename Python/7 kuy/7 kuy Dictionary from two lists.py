'''
There are two lists, possibly of different lengths. The first one
consists of keys, the second one consists of values. Write a function
createDict(keys, values) that returns a dictionary created from keys
and values. If there are not enough values, the rest of keys should
have a None (JS null)value. If there not enough keys,
just ignore the rest of values.

Example 1:

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
Example 2:

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
'''

def create_dict(keys, values):
    d = {}
    for i in range(len(keys)):
        try:
            d[keys[i]] = values[i]
        except:
            d[keys[i]] = None
    return d
	
# smart solution

def create_dict(keys, values):
    return dict.fromkeys(keys) | dict(zip(keys,values))

'''
Функция dict.fromkeys(keys) создает новый словарь, где ключами являются элементы списка keys, а значениями является None.
Это гарантирует, что каждый ключ будет присутствовать в словаре, даже если в списке values не хватает значений.

Функция zip(keys, values) создает пары ключ-значение из двух списков.
Затем dict(zip(keys, values)) преобразует эти пары в словарь.

Оператор | выполняет объединение двух словарей. Если ключ присутствует в обоих словарях,
то значение этого ключа в результирующем словаре будет взято из второго словаря
(в данном случае из dict(zip(keys, values))). Это означает, что для каждого ключа
будет использовано соответствующее значение из списка values, если оно есть.
Если для ключа нет значения в списке values, то будет использовано значение
None из словаря dict.fromkeys(keys).'''
	
	

def test_create_dict():
    assert create_dict(['a', 'b', 'c', 'd'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3, 'd': None}
    assert create_dict(['a', 'b', 'c'], [1, 2, 3, 4]) == {'a': 1, 'b': 2, 'c': 3}
    assert create_dict([], []) == {}
    assert create_dict([], [1]) == {}
    assert create_dict(['a'], []) == {'a':None}
	print("All tests passed!")
	

test_create_dict()