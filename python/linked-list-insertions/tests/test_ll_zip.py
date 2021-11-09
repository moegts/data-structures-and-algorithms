import pytest

from linked_list_insertions import __version__
from linked_list_insertions.ll_zip import zip_Lists
from linked_list_insertions.linked_list import Linkedlist


def test_version(): assert __version__ == '0.1.0'

def test_equal():
    test1, test2 = Linkedlist(), Linkedlist()

    test1.append(10) ; test1.append(30)
    test1.append(20) ; test2.append(50)
    test2.append(90) ; test2.append(40)

    zip_Lists(test1,test2)

    expected, actual = "{10}-> {50}-> {30}-> {90}-> {20}-> {40}-> NULL", test1.__str__()
    assert expected == actual


def test_not_equal():
    test1, test2 = Linkedlist(), Linkedlist()
    test1.append(11) ; test1.append(33)
    test2.append(50) ; test2.append(90)
    test2.append(40)

    zip_Lists(test1,test2)

    expected, actual = "{11}-> {50}-> {33}-> {90}-> {40}-> NULL", test1.__str__()
    assert expected == actual



def test_not_equal2():
    test1, test2 = Linkedlist(), Linkedlist()

    test1.append(12) ; test1.append(32)
    test1.append(22) ; test2.append(52)
    test2.append(92)

    zip_Lists(test1,test2)

    expected, actual ="{12}-> {52}-> {32}-> {92}-> {22}-> NULL", test1.__str__()
    assert expected == actual