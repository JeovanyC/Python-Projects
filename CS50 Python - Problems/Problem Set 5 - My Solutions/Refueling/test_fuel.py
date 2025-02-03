from fuel import getFuel

def test100():
    assert getFuel(1 / 1) == "F"

def test50():
    assert getFuel(1 / 2) == "50%"

def test0():
    assert getFuel(0 / 1) == "E"