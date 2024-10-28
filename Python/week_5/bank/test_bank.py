import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def h_test():
    assert value("hi") == 20
    assert value("hi there") == 20
    assert value("howdy") == 100

def other():
    assert value("good morning") == 100
    assert value("Whats up") == 100
    assert value("welcome ") == 100
    assert value(" ") == 100

