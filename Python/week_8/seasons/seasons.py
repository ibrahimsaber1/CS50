from datetime import date
import inflect
import sys


def main():
    birth_date_str = input("Date of Birth (YYYY-MM-DD): ")
    birth_day = date_validation(birth_date_str)
    age_in_min = calculate_age_in_min(birth_day)
    print(num_into_word(age_in_min).capitalize(), "minutes")



def num_into_word(min):
    p = inflect.engine()
    return p.number_to_words(min, andword="")

def calculate_age_in_min(birth_day):
    today = date.today()
    age_in_days = (today - birth_day).days
    age_in_min = age_in_days * 24 * 60
    return age_in_min

def date_validation(user_input):
    try:
        year, month, day = map(int, user_input.split("-"))
        return date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")


if __name__ == '__main__':
    main()
