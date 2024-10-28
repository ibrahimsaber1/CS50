import pytest
from um import count


def test_single_um():
    assert count("um") == 1

def test_alot_of_um():
    assert count("um um um um") == 4

def test_defferent_text():
    assert count("hi there, um my name is ibrahim") == 1
    assert count("hi there, um... my name is ibrahim") == 1
    assert count("hi there, um? my name is ibrahim") == 1

def test_um_with_mixed_case():
    assert count("UM um Um uM") == 4

def test_um_as_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("summer") == 0


def test_no_um():
    assert count("This sentence has no relevant word.") == 0

def test_um_with_surrounding_text():
    assert count("Hello, um, world!") == 1
    assert count("Um, thanks, um...") == 2

def test_empty_string():
    assert count("") == 0

def test_um_with_newlines():
    assert count("um\num\num") == 3

def test_um_with_tabs_and_spaces():
    assert count("um\tum  um") == 3
