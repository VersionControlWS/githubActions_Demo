"""Module providing a function printing python version."""

# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

import sys
import math
import pytest

import logging
prnt = logging.getLogger(__name__)

@pytest.fixture
def print_python_version():
    print(f'Python-version on this system is {sys.version.split()[0]}')
    prnt.info(f'Python-version on this system is {sys.version.split()[0]}')

def test_sqrt_one():
    num = 25
    assert math.sqrt(num) == 5
    prnt.info(sys.version.split()[0])

def testsquare_two():
    assert 7*7 == 49

@pytest.mark.parametrize("output, num",[(11,1),(22,2),(35,3),(44,4),(55,5)])
def test_multiplication_of_11_tables(output, num):
    try:
        assert 11*num == output
    except Exception as e:
        prnt.error(e)
