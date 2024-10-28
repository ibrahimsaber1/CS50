from datetime import date
import pytest

from seasons import num_into_word,calculate_age_in_min,date_validation


def test_calculate_age_in_minutes():
    assert calculate_age_in_min(date(2020, 1, 1)) == 2528640  # 365 days in a non-leap year
    assert calculate_age_in_min(date(2019, 1, 1)) == 3054240  # 2019 was a leap year
    assert calculate_age_in_min(date(2000, 7, 15)) == 12765600  # this is my birth day :)


def test_parse_date():
    assert date_validation("2000-01-01") == date(2000, 1, 1)
    with pytest.raises(SystemExit):
        date_validation("01-01-2000")  # Invalid format should raise a SystemExit


def test_minutes_to_words():
    assert num_into_word(525600) == "five hundred twenty-five thousand, six hundred"
    assert num_into_word(1051200) == "one million, fifty-one thousand, two hundred"
    assert num_into_word(12765600) == "twelve million, seven hundred sixty-five thousand, six hundred"


print(calculate_age_in_min(date(2020, 1, 1)))
