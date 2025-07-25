from fuel import convert, gauge
from pytest import raises


# Test convert 
def test_convert(): 
    assert convert("2/3") == 67 
    with raises(ValueError): 
        assert convert("cat/dog") 
    with raises(ValueError): 
        assert convert("3/2") 
    with raises(ZeroDivisionError): 
        assert convert("0/0")


# Test negative
def test_negative():
    with raises(ValueError):
        convert("-1/2")


# Test gauge
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"