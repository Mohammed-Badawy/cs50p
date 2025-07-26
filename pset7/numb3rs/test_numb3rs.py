from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True


def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") ==  False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    

