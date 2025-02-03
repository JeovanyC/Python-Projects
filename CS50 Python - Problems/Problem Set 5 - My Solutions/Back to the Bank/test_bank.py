from bank import value

def testHello():
    assert value("Hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("hello") == "$0"

def testHey():
    assert value("Hey") == "$20"
    assert value("hey") == "$20"
    assert value("HEy") == "$20"

def testOthers():
    assert value("What is up?") == "$100"
    assert value("random text") == "$100"
    assert value("") == "$100"

def testAnything():
    assert value("12345") == "$100"
    assert value("!@#$%^") == "$100"
    assert value("Hello123") == "$0" 