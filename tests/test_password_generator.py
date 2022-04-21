import pytest
from src import password_checker, password_generator


@pytest.mark.parametrize('case', (1, 2, 3, 4, 5))
def test_generate_password(case):
    password = password_generator.generate_password()
    assert len(password_checker.check_password(password)) == 6
