from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("127.22.14.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_invalied():
    assert validate("256.562.20.0") == False
    assert validate("127.15.20.500") == False
    assert validate("127.14.5") == False
    assert validate("tree") == False
    assert validate("127.14.5.lol") == False

