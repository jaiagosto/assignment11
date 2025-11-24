# app/operations.py
"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, and division of two numbers.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers and return the result."""
    result = a + b
    return result


def subtract(a: Number, b: Number) -> Number:
    """Subtract the second number from the first and return the result."""
    result = a - b
    return result


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers and return the product."""
    result = a * b
    return result


def divide(a: Number, b: Number) -> float:
    """Divide the first number by the second and return the quotient."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    
    result = a / b
    return result
