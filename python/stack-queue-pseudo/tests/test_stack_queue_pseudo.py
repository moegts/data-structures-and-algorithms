from stack_queue_pseudo import __version__
from stack_queue_pseudo.queue_with_stacks import PseudoQueue


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_singl():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(21)
    assert 21 == Pseudoqueue.rear

def test_enqueue_multiple():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(21)
    Pseudoqueue.enqueue(22) ; Pseudoqueue.enqueue(23)
    assert 23 == Pseudoqueue.rear


def test_dequeue_ps():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(1) ; Pseudoqueue.enqueue(2)
    Pseudoqueue.enqueue(3) ; Pseudoqueue.dequeue()
    Pseudoqueue.dequeue()
    assert 3 == Pseudoqueue.dequeue()


def test_dequeue_empty():
    Pseudoqueue = PseudoQueue()
    assert None == Pseudoqueue.dequeue() 