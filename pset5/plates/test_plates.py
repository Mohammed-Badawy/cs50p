from plates import is_valid


# Test first two chars
def test_start_with_alphabetical():
    assert is_valid("2A") == False
    assert is_valid("AA") == True
    assert is_valid("22") == False
    

# Test length
def test_length():
    assert is_valid("AAA222") == True
    assert is_valid("AAA2222") == False
    assert is_valid("A") == False
    assert is_valid("AAA") == True


# Test first digit is zero
def test_first_digit_not_zero():
    assert is_valid("AAA222") == True
    assert is_valid("AAA022") == False


# Test contains alphabetical after digits
def test_no_letters_after_digits():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


# Test punctuations chars @ _ . etc
def test_contains_non_alnum_chars():
    assert is_valid("AAA@_2") == False