
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


