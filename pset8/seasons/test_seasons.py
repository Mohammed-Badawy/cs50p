from seasons import convert_minutes


# Test convert date to minutes
def test_convert_minutes():
    assert convert_minutes(
        "2024-07-27") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_minutes(
        "2023-07-27") == "One million, fifty-two thousand, six hundred forty minutes"

