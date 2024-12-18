"""
prime.py -- Write the application code here
"""

def generate_prime_factors(n):
    if not isinstance(n, int):
        raise ValueError("Not an integer")
    if n == 1:
        return []
    return []