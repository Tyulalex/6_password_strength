import string
import re

PASSWORD_BLACKLIST = [
    "qwerty",
    "Password1\". Ааа!",
    "password",
    "12345678",
    "(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d",
    "[\+7|8][0-9]{11}"
]

PERSONAL_INFO = {
    "name": "", "bdate": "", "company": ""
}


def is_password_in_blacklist(password):
    return not any(
        re.match(pattern, password, re.IGNORECASE
                 ) for pattern in PASSWORD_BLACKLIST
        ) and not any(
        re.match(pattern, password, re.IGNORECASE
                 ) for pattern in PERSONAL_INFO.values()
        )


def get_list_of_password_criterias():
    return [
        lambda user_password: any(
            character.isupper() for character in user_password
        ) and any(
            character.islower() for character in user_password
        ),
        lambda user_password: len(user_password) > 10,
        lambda user_password: any(
            character.isdigit() for character in user_password
        ),
        lambda user_password: any(
            character in string.punctuation for character in user_password
        ),
        lambda user_password: is_password_in_blacklist(user_password)
    ]


def get_password_strength(password):
    strentgh = 0
    criterias_to_be_satisfied_list = get_list_of_password_criterias()
    for is_satisfied_criteria in criterias_to_be_satisfied_list:
        if is_satisfied_criteria(password):
            strentgh += 2
    return strentgh


if __name__ == '__main__':
    PERSONAL_INFO['name'] = input("Как Вас зовут?\n")
    PERSONAL_INFO['bdate'] = input("Введите Дату рождения\n")
    PERSONAL_INFO['company'] = input("Имя компании, где вы работаете\n")
    raw_user_password = input("Введите пароль:\n")
    print("Уровень вашего пароля:", get_password_strength(raw_user_password))
