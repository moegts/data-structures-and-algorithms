from graph_depth_first import __version__
from graph_depth_first.queue_and_stack import *
from graph_depth_first.code import *


def test_version():
    assert __version__ == "0.1.0"


def test_depth_first_search1():

    graph = {
        "A": ["B", "C", "D"],
        "B": ["E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": ["I"],
        "F": ["J"],
    }

    assert graph_depth_first(graph, "A") == "A D H C G F J B E I"


def test_depth_first_search2():

    graph = {
        "A": ["B", "D"],
        "B": [
            "C",
            "D",
        ],
        "C": ["G"],
        "D": ["E", "H", "F"],
        "H": ["F"],
    }

    assert graph_depth_first(graph, "A") == "A D F H E B C G"


def test_depth_first_search3():

    graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

    assert graph_depth_first(graph, "5") == "5 7 8 3 4 2"
