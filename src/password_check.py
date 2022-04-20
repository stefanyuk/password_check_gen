import argparse
import colorama
import string

error_messages = {
    'lower_upper': 'Password must contain both lowercase and uppercase characters',
    'digit': 'Password must contain at least one digit',
    'punctuation_letter': 'Password must contain at least one punctuation letter (!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~.)',
    'length': 'Password must be at least 14 character long'
}


def create_parser():
    """
    Initializes parser
    :return: parser object
    """
    parser = argparse.ArgumentParser(description='Write a password to perform it\'s verification')
    parser.add_argument('--password', type=str, help='password that needs to be verified', required=True)

    return parser


def check_password(password: str):
    """
    Verifies whether provided by user password complies with defined constraints
    :return:
    """
    satisfied_constraints = []

    if len(password) > 14:
        satisfied_constraints.append('length')

    for character in set(password):
        if 'upper' not in satisfied_constraints and character.isupper():
            satisfied_constraints.append('upper')
        elif 'lower' not in satisfied_constraints and character.islower():
            satisfied_constraints.append('lower')
        elif 'digit' not in satisfied_constraints and character.isdigit():
            satisfied_constraints.append('digit')
        elif 'punctuation_letter' not in satisfied_constraints and character in string.punctuation:
            satisfied_constraints.append('punctuation_letter')
        elif not error_messages.keys() - satisfied_constraints:
            break

    return satisfied_constraints


def show_results(satisfied_constraints: list):
    """

    :param satisfied_constraints:
    :return:
    """
    password_errors = error_messages.keys() - satisfied_constraints
    if password_errors:
        print('Weak password')
        for error in password_errors:
            print(f'- {error_messages[error]}')
    else:
        print('Strong password')


def main():
    # args = create_parser().parse_args()
    user_input = input('Please provide a password: ')
    res = check_password(user_input)
    show_results(res)


main()
