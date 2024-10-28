from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_shorten_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_shorten_numbers():
    assert shorten("12345") == "12345"

def test_shorten_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_vowels_only():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_with_spaces():
    assert shorten("CS50 is awesome") == "CS50 s wsm"
