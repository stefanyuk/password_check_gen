import argparse
import colorama
from colorama import Fore
import string

error_messages = {
    'lower_upper': 'Password must contain both lowercase and uppercase characters',
    'digit': 'Password must contain at least one digit',
    'punctuation_char': f'Password must contain at least one punctuation letter ({string.punctuation})',
    'length': 'Password must be at least 14 character long'
}


def create_parser():
    """
    Initializes parser
    :return: parser object
    """
    parser = argparse.ArgumentParser(description='Write a password to perform it\'s verification')
    parser.add_argument('password', type=str, help='password that needs to be verified')

    return parser


def check_password(password: str):
    """
    Verifies whether password provided by user complies with defined constraints
    :param password: string that needs to be verified
    :return: list of satisfied constraints during check
    """
    satisfied_constraints = []

    if len(password) >= 14:
        satisfied_constraints.append('length')

    for character in set(password):
        if 'upper' not in satisfied_constraints and character.isupper():
            satisfied_constraints.append('upper')
            if 'lower' in satisfied_constraints:
                satisfied_constraints.append('lower_upper')
        elif 'lower' not in satisfied_constraints and character.islower():
            satisfied_constraints.append('lower')
            if 'upper' in satisfied_constraints:
                satisfied_constraints.append('lower_upper')
        elif 'digit' not in satisfied_constraints and character.isdigit():
            satisfied_constraints.append('digit')
        elif 'punctuation_char' not in satisfied_constraints and character in string.punctuation:
            satisfied_constraints.append('punctuation_char')
        elif not error_messages.keys() - satisfied_constraints:
            break

    return satisfied_constraints


def show_results(satisfied_constraints: list):
    """
    Prints either the positive result of the password check or negative result and appropriate error messages
    :param satisfied_constraints: list of constraints that were satisfied during password check
    """
    password_errors = error_messages.keys() - satisfied_constraints
    if password_errors:
        print(Fore.RED + 'Weak password:')
        for error in password_errors:
            print(f'- {error_messages[error]}')
    else:
        print(Fore.GREEN + 'Strong password')


def main():
    colorama.init()
    args = create_parser().parse_args()
    res = check_password(args.password)
    show_results(res)


if __name__ == '__main__':
    main()
