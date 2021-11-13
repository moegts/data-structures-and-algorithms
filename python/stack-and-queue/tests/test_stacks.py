from stack_and_queue.stack import Stack

def test_push():
    stack = Stack() ; stack.push(30)
    excepted = stack.top.value
    assert excepted == 30


def test_push2():
    stack = Stack()
    stack.push(12) ; stack.push(1)
    excepted = stack.top.value
    assert excepted == 1

def test_pop():
    stack = Stack()
    stack.push(22) ; stack.push(1)
    actual = stack.pop() ; expected = 1
    assert actual == expected

def test_pop2():
    stack = Stack()
    stack.push(1) ; stack.push(20)
    stack.pop() ; stack.pop()
    actual = stack.top ; expected = None
    assert actual == expected


def test_peek():
    stack = Stack()
    stack.push(9)
    stack.push(7)
    expected = 7
    actual = stack.peek()
    assert actual == expected


def test_init_empty():
    stack = Stack()
    expected = None
    actual = stack.top
    assert expected == actual


def test_raise_stack():
    stack = Stack()
    expected = "Stack is Empty"
    assert expected == stack.peek()


