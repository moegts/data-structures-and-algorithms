from stack_queue_brackets import __version__
from stack_queue_brackets.brackets import validateBrackets

def test_version():
    assert __version__ == '0.1.0'

def test_one():
    expected = validateBrackets('{}')
    acutal = True
    assert expected == acutal

def test_two():
    expected = validateBrackets('{}(){}')
    acutal = True
    assert expected == acutal

def test_three():
    expected = validateBrackets('()[[Extra Characters]]')
    acutal = True
    assert expected == acutal

def test_four():
    expected = validateBrackets('(){}[[]]')
    acutal = True
    assert expected == acutal

def test_five():
    expected = validateBrackets('{}{Code}[Fellows](())')
    acutal = True
    assert expected == acutal

def test_six():
    expected = validateBrackets('[({}]')
    acutal = False
    assert expected == acutal

def test_seven():
    expected = validateBrackets('(](')
    acutal = False
    assert expected == acutal

def test_eight():
    expected = validateBrackets('{(})')
    acutal = False
    assert expected == acutal