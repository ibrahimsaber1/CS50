
import pytest
from fuel import convert, gauge

def test_convert_valid_inputs():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("0/1") == 0
    assert convert("100/100") == 100

def test_convert_invalid_inputs():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("3/2")  # Numerator greater than denominator
    with pytest.raises(ValueError):
        convert("")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_typical():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"
