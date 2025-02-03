from twttr import shorten

def testVowels():
    assert shorten("bcdfg") == "bcdfg"

def testLowerCase():
    assert shorten("aeiou") == ""

def testUpperCase():
    assert shorten("AEIOU") == ""

def testEmptyString():
    assert shorten("") == ""

def testPontuationCharacteres():
    assert shorten("12345!@#$%") == "12345!@#$%"