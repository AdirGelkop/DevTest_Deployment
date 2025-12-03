import pytest

def get_level(years):
    if years < 2:
        return "Junior"
    elif years < 5:
        return "Mid"
    else:
        return "Senior"

@pytest.mark.parametrize("years, expected_level", [
    (1, "Junior"),
    (3, "Mid"),
    (5, "Senior"),
    (0, "Junior"),
    (4, "Mid"),
    (10, "Senior"),
])

def test_get_level(years, expected_level):
    assert get_level(years) == expected_level

