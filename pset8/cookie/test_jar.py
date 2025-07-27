from jar import Jar
from pytest import raises


# Test initializing new jar
def test_init():
    j = Jar()
    assert j._capacity == 12
    j = Jar(14)
    assert j._capacity == 14

    # Raise ValueError if caacity is negative int
    with raises(ValueError):
        j = Jar(-1)        


# Test str method
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# Test deposit method
def test_deposit():
    j = Jar()
    j.deposit(1)
    assert j._size == 1
    j.deposit(11)
    assert j._size == 12

    # Raise ValueError if capacity isn't enough
    with raises(ValueError):
        j.deposit(1)


# Test withdraw method
def test_withdraw():
    j = Jar()
    j.deposit(12)
    j.withdraw(11)
    assert j._size == 1
    j.withdraw(1)
    assert j._size == 0

    # Raise ValueError if there aren't enough cookies
    with raises(ValueError):
        j.withdraw(1)