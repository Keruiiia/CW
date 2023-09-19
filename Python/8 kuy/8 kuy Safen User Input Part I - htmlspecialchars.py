'''
Your mission is to implement a function that converts the following potentially harmful characters:

< --> &lt;
> --> &gt;
" --> &quot;
& --> &amp;
'''

def html_special_chars(data): 
    d = {
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "&": "&amp;",
    }
    s = ''
    for char in data:
        if char in d:
            s += d[char]
        else:
            s += char
    return s
	
# smart_solustion
def html_special_chars(data): 
    return data.translate(str.maketrans({'<':'&lt;','>':'&gt;','"':'&quot;','&':'&amp;'}))
	
def test_html_special_chars():
	assert html_special_chars("<h2>Hello World</h2>") == "&lt;h2&gt;Hello World&lt;/h2&gt;"
    assert html_special_chars("Hello, how would you & I fare?") == "Hello, how would you &amp; I fare?"
    assert html_special_chars('How was "The Matrix"?  Did you like it?') == 'How was &quot;The Matrix&quot;?  Did you like it?'
	print("All tests passed!")
	
test_html_special_chars()