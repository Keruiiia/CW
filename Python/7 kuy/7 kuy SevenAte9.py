'''
Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"
'''

def seven_ate9(str_):
    lst, new_s = [], ""
    for i, char in enumerate(str_):
        if char == "7" and str_[i-1] == "9" and str_[i-2] == "7":
            lst.append(i-1)
    for i, char in enumerate(str_):
        if i not in lst:
            new_s += char
    return new_s
	
#smart solution

def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_


def test_seven_ate9():
    assert seven_ate9('165561786121789797') == '16556178612178977'
    assert seven_ate9('797') == '77'
    assert seven_ate9('7979797') == '7777'
    assert seven_ate9('16797') == '1677'
    print("All tests passed!")


test_seven_ate9()