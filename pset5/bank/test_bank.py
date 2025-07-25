from bank import value


# Check start with hello
def test_start_with_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


# Check start with h
def test_start_with_h():
    assert value("How you doing?") == 20
    assert value("how you doing?") == 20


# Check start with any other words
def test_start_with_other_words():
    assert value("What's up?") == 100
    assert value("what's happening?") == 100