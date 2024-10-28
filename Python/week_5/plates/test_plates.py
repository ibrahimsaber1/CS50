from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_starting_letters():
    assert is_valid("AB123") == True
    assert is_valid("1ABC") == False

def test_number_placement():
    assert is_valid("ABC123") == True
    assert is_valid("AB12C3") == False
    assert is_valid("AB0123") == False

def test_allowed_characters():
    assert is_valid("ABC!@#") == False
    assert is_valid("ABC 123") == False

def test_numbers_after_letters():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCD1E") == False

def test_no_leading_zero():
    assert is_valid("AB012") == False
    assert is_valid("AB123") == True

def test_starts_with_two_letters():
    assert is_valid("AB123") == True
    assert is_valid("A1234") == False
    assert is_valid("12345") == False
    assert is_valid("1ABCD") == False
    assert is_valid("!ABCD") == False
