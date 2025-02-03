from numb3rs import validate

def test_ValidTrue():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True

def test_ValidFalse():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1") == False
    assert validate("192.168.01.1") == False
    assert validate("999.999.999.999") == False
    assert validate("192.168.-1.1") == False

def test_ValidString():
    assert validate("Chair") == False
    assert validate("House") == False
    assert validate("Cat") == False
    assert validate("True") == False
    assert validate("False") == False