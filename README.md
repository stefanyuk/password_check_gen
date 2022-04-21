# Password generator and password checker

## Description

This is a command line application that allows you to perform validation of the password. Also, you may create your own password.
Application will perform validation based on the following constraints:

1. The password contains both lowercase and uppercase characters
2. The password contains at least one digit
3. The password contains at least one punctuation character
4. The password is at least 14 characters long

## Technologies
- Python 3.8 or higher

## Modules that are used
- argparse
- colorama
- pytest

***
## Setup on Linux

1. Clone the repo

> git clone https://github.com/stefanyuk/password_check_gen.git

2. Create virtual environment in project
> cd password_check_gen/

> python3 -m venv venv

> source venv/bin/activate

3. Install project requirements

> pip install -r requirements.txt

***
## Usage

If you want to validate a password type the following command

> python3 <path_to_the_file_password_checker.py> your_password

If you want to create a new password type the following command

> python3 <path_to_the_file_password_generator.py>