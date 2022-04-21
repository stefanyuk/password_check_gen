import string
import random
from itertools import cycle, islice


def generate_password():
    """
    Generates random password for the user
    :return: generated password
    """
    characters = (string.punctuation, string.ascii_lowercase, string.ascii_uppercase, string.digits)
    password = [random.choice(char_set) for char_set in islice(cycle(characters), 14)]
    return ''.join(password)


if __name__ == '__main__':
    print(generate_password())
