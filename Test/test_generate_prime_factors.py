
import pytest
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent))

from prime import generate_prime_factors

def test_non_integer_input():
    with pytest.raises(ValueError):
        generate_prime_factors("not an integer")
    with pytest.raises(ValueError):
        generate_prime_factors(1.5)

def test_prime_factors_of_1():
    assert generate_prime_factors(1) == []


def test_prime_factors_of_2():
    assert generate_prime_factors(2) == [2]

def test_prime_factors_of_3():
    assert generate_prime_factors(3) == [3]

def test_prime_factors_of_4():
    assert generate_prime_factors(4) == [2, 2]

def test_prime_factors_of_6():
    assert generate_prime_factors(6) == [2, 3]

def test_prime_factors_of_8():
    assert generate_prime_factors(8) == [2, 2, 2]

def test_prime_factors_of_9():
    assert generate_prime_factors(9) == [3, 3]

