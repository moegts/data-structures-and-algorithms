from stack_and_queue.queue import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert expected == actual


def test_enqueue2():
    queue = Queue()
    queue.enqueue('mohammad') ; queue.enqueue('mohamma')
    actual = queue.front.next.value
    expected = 'mohamma'
    assert expected == actual


def test_dequeue():
    queue = Queue()
    queue.enqueue(55) ; queue.enqueue(300)
    queue.dequeue()
    actual = queue.front.value
    expected = 300
    assert expected == actual


def test_peek_dedueue():
    queue = Queue()
    queue.enqueue(66) ; queue.enqueue(15)
    expected = 66 ; actual = queue.peek()
    assert actual == expected


def test_empty_queue():
    queue = Queue()
    queue.enqueue(1) ; queue.enqueue(29)
    queue.dequeue() ; queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected


def test_init_empty_queue():
    queue = Queue()
    expected = None
    assert expected == queue.front


def test_raise_queue():
    queue = Queue()
    expected = "Queue is Empty"
    assert expected == queue.peek()
