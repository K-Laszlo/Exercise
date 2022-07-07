import pytest

from day4.teszteles.tut2.myapp.sample import validate_age


def test_validate_age_valid_age():
    actual = validate_age(10)
    excepted = 10
    assert excepted == actual


def test_validate_age_invalid_age():  # check Value error and message
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    assert str(exc_info.value) == 'Age can not be less than 0'


def test_validate_age_invalid_age2():  # check Value error and message with inbuilt function
    with pytest.raises(ValueError, match='Age can not be less than 0'):
        validate_age(-1)
