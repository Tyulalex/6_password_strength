import string
import re
import getpass

def password_has_upper_case(password):
    return any(character.isupper() for character in password)


def password_has_lower_case(password):
    return any(character.islower() for character in password)


def password_has_any_digit(password):
    return any(character.isdigit() for character in password)


def password_has_special_symbols(password):
    return any(character in string.punctuation for character in password)


def password_does_not_match_calendar_dates(password):
    r_exp = "(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d"
    return not re.match(r_exp, password)


def password_does_not_match_phone_numbers(password):
    return not re.match(".*[\+7|8][0-9]{11}.*", password)


def password_has_any_letter(password):
    return any(character.isalpha() for character in password)


def password_does_not_match_licence_plate(password):
    return not re.match("[aA-zZ]\d{3}[aA-zZ]{2}\d{1,3}", password)


def is_password_length_more_than_given_length(password, length=10):
    return len(password) > length


def get_list_of_password_criterias():
    return [
        is_password_length_more_than_given_length,
        password_does_not_match_licence_plate,
        password_has_any_letter,
        password_does_not_match_phone_numbers,
        password_does_not_match_calendar_dates,
        password_has_special_symbols,
        password_has_any_digit,
        password_has_lower_case,
        password_has_upper_case
    ]


def get_password_strength(password):
    strentgh = 10
    criterias_to_be_satisfied_list = get_list_of_password_criterias()
    for is_criteria_satisfied in criterias_to_be_satisfied_list:
        if not is_criteria_satisfied(password):
            strentgh -= 1
    return strentgh if strentgh else 1


if __name__ == '__main__':
    max_strengh = 10
    raw_user_password = getpass.getpass("Введите пароль:\n")
    digit_password_level = get_password_strength(raw_user_password)
    print(
        "Оценка паролей по цифровой шкале:10 - очень крутой, 1 - очень слабый")
    print("Уровень вашего пароля:", get_password_strength(raw_user_password))
