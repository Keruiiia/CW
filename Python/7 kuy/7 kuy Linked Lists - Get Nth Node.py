'''
Implement a GetNth() function that takes a linked list and an integer index and returns
the node stored at the Nth index position. GetNth() uses the C numbering convention that
the first node is index 0, the second is index 1, ... and so on.

So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index, i=0):
    if node is None:
        raise IndexError
    else:
        return node if index == i else get_nth(node.next, index, i + 1)