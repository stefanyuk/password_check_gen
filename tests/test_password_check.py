import argparse
import pytest
from unittest.mock import patch
from src import password_check


def test_create_parser():
    assert isinstance(password_check.create_parser(), argparse.ArgumentParser)


@pytest.mark.parametrize('password', ['kWU*123DeW%NMsE', "sbr1J'sC|d/~C`", '"1qV^.YG/ScM]/M'])
def test_check_valid_password(password):
    assert len(password_check.check_password(password)) == 6


@pytest.mark.parametrize('password', ['kWU*DeW%NMsE', "sbrJ'sC|d/~C", '"qV^.YG/ScM]/M'])
def test_check_password_without_digit(password):
    assert 'digit' not in password_check.check_password(password)


@pytest.mark.parametrize('password', ['kWUDeWNMsEaaas22', "sbrJsCdC123asd", 'qVYGScMMassd123123'])
def test_check_password_without_punctuation_char(password):
    assert 'punctuation_letter' not in password_check.check_password(password)


@pytest.mark.parametrize('password', ['dma".()*asdasd22', "2123AASDSQWWQQ.", 'qc.123123assd123123'])
def test_check_password_without_upper_lower_char(password):
    assert 'lower_upper' not in password_check.check_password(password)


@pytest.mark.parametrize('password', ['kWU*DeW5%9NMsE', "sbr1J'sC|d/~C`", '"1qV^.YG/ScM]/M'])
@patch('builtins.print')
@patch('src.password_check.argparse.ArgumentParser.parse_args')
def test_main_with_valid_password(parser_mock, print_mock, password):
    parser_mock.return_value = argparse.Namespace(password=password)
    password_check.main()
    assert print_mock.call_count == 1


@pytest.mark.parametrize('password', ['dma".()*asdasd22', "2123AASDSQWWQQ.", 'sbrJsCdC123asd'])
@patch('builtins.print')
@patch('src.password_check.argparse.ArgumentParser.parse_args')
def test_main_with_invalid_password_1_error(parser_mock, print_mock, password):
    parser_mock.return_value = argparse.Namespace(password=password)
    password_check.main()
    assert print_mock.call_count == 2


@pytest.mark.parametrize('password', ['dma".()*asdasdss', "2123AASDSQWWQQ", 'sbrJsCdCaaasddd'])
@patch('builtins.print')
@patch('src.password_check.argparse.ArgumentParser.parse_args')
def test_main_with_invalid_password_2_errors(parser_mock, print_mock, password):
    parser_mock.return_value = argparse.Namespace(password=password)
    password_check.main()
    assert print_mock.call_count == 3


@pytest.mark.parametrize('password', ['qwerty', "rtyuw", 'asdasdww'])
@patch('builtins.print')
@patch('src.password_check.argparse.ArgumentParser.parse_args')
def test_main_with_invalid_password_4_errors(parser_mock, print_mock, password):
    parser_mock.return_value = argparse.Namespace(password=password)
    password_check.main()
    assert print_mock.call_count == 5
