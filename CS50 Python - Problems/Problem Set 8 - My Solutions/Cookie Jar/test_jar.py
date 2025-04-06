from jar import Jar
import pytest

def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.size == 10
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.size == 12

    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.size == 10
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    jar.size == 7
    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.size == 6
    jar.withdraw(6)
    assert str(jar) == ""

    with pytest.raises(ValueError):
        jar.withdraw(1)

def test_capacity():
    jar1 = Jar(2)
    jar2 = Jar(30)
    jar3 = Jar(15)
    jar4 = Jar(9)

    assert jar1.capacity == 2
    assert jar2.capacity == 30 
    assert jar3.capacity == 15
    assert jar4.capacity == 9

def test_init():
    jar1 = Jar(2)

    with pytest.raises(ValueError):
        Jar(-15)

    with pytest.raises(ValueError):
        Jar(4.2)

    with pytest.raises(ValueError):
        Jar(0)