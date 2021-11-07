from linked_list import __version__
from linked_list.linkedLists import LinkedList


def test_version():assert __version__ == '0.1.0'

def test_Linkedlist_empty():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual

def test_includes_true():
    ll = LinkedList()
    ll.insert('first')
    ll.insert('second')
    ll.insert('third')
    expected = True
    actual = ll.includes('first')
    assert expected == actual

def test_insert_multiple():
    ll = LinkedList()
    ll.insert('first')
    ll.insert(66)
    ll.insert('second')
    expected = '{second}-> {66}-> {first}-> NULL'
    actual = ll.__str__()
    assert expected == actual

def test_insert_one():
    ll = LinkedList()
    ll.insert('first')
    expected = '{first}-> NULL'
    actual = ll.__str__()
    assert expected == actual



def test_includes_false():
    ll = LinkedList()
    ll.insert('first')
    ll.insert('second')
    ll.insert('third')
    expected = False
    actual = ll.includes('fourth')
    assert expected == actual




