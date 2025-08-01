from pytest import raises
from working import convert


# Test correct format
def test_correct_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


# Test wrong format omits "to"
def test_ommit_to():
    with raises(ValueError):
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")


# Test out of range time
def test_out_of_range():
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM")