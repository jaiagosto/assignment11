# tests/integration/test_calculation.py
"""
Integration Tests for Polymorphic Calculation Models
"""

import pytest
import uuid

from app.models.calculation import (
    Calculation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
)


def dummy_user_id():
    """Generate a random UUID for testing purposes."""
    return uuid.uuid4()


# Tests for Individual Calculation Types
def test_addition_get_result():
    """Test that Addition.get_result returns the correct sum."""
    inputs = [10, 5, 3.5]
    addition = Addition(user_id=dummy_user_id(), inputs=inputs)
    result = addition.get_result()
    assert result == sum(inputs)


def test_subtraction_get_result():
    """Test that Subtraction.get_result returns the correct difference."""
    inputs = [20, 5, 3]
    subtraction = Subtraction(user_id=dummy_user_id(), inputs=inputs)
    result = subtraction.get_result()
    assert result == 12


def test_multiplication_get_result():
    """Test that Multiplication.get_result returns the correct product."""
    inputs = [2, 3, 4]
    multiplication = Multiplication(user_id=dummy_user_id(), inputs=inputs)
    result = multiplication.get_result()
    assert result == 24


def test_division_get_result():
    """Test that Division.get_result returns the correct quotient."""
    inputs = [100, 2, 5]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    result = division.get_result()
    assert result == 10


def test_division_by_zero():
    """Test that Division.get_result raises ValueError when dividing by zero."""
    inputs = [50, 0, 5]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division.get_result()


# Tests for Polymorphic Factory Pattern
def test_calculation_factory_addition():
    """Test the Calculation.create factory method for addition."""
    inputs = [1, 2, 3]
    calc = Calculation.create(
        calculation_type='addition',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    assert isinstance(calc, Addition)
    assert isinstance(calc, Calculation)
    assert calc.get_result() == sum(inputs)


def test_calculation_factory_subtraction():
    """Test the Calculation.create factory method for subtraction."""
    inputs = [10, 4]
    calc = Calculation.create(
        calculation_type='subtraction',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    assert isinstance(calc, Subtraction)
    assert calc.get_result() == 6


def test_calculation_factory_multiplication():
    """Test the Calculation.create factory method for multiplication."""
    inputs = [3, 4, 2]
    calc = Calculation.create(
        calculation_type='multiplication',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    assert isinstance(calc, Multiplication)
    assert calc.get_result() == 24


def test_calculation_factory_division():
    """Test the Calculation.create factory method for division."""
    inputs = [100, 2, 5]
    calc = Calculation.create(
        calculation_type='division',
        user_id=dummy_user_id(),
        inputs=inputs,
    )
    assert isinstance(calc, Division)
    assert calc.get_result() == 10


def test_calculation_factory_invalid_type():
    """Test that Calculation.create raises a ValueError for unsupported types."""
    with pytest.raises(ValueError, match="Unsupported calculation type"):
        Calculation.create(
            calculation_type='modulus',
            user_id=dummy_user_id(),
            inputs=[10, 3],
        )


def test_calculation_factory_case_insensitive():
    """Test that the factory is case-insensitive."""
    inputs = [5, 3]
    
    for calc_type in ['addition', 'Addition', 'ADDITION', 'AdDiTiOn']:
        calc = Calculation.create(
            calculation_type=calc_type,
            user_id=dummy_user_id(),
            inputs=inputs,
        )
        assert isinstance(calc, Addition)
        assert calc.get_result() == 8


# Tests for Input Validation
def test_invalid_inputs_for_addition():
    """Test that providing non-list inputs to Addition.get_result raises error."""
    addition = Addition(user_id=dummy_user_id(), inputs="not-a-list")
    with pytest.raises(ValueError, match="Inputs must be a list of numbers."):
        addition.get_result()


def test_invalid_inputs_for_subtraction():
    """Test that providing fewer than two numbers raises a ValueError."""
    subtraction = Subtraction(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(
        ValueError,
        match="Inputs must be a list with at least two numbers."
    ):
        subtraction.get_result()


def test_invalid_inputs_for_multiplication():
    """Test that Multiplication requires at least two inputs."""
    multiplication = Multiplication(user_id=dummy_user_id(), inputs=[5])
    with pytest.raises(
        ValueError,
        match="Inputs must be a list with at least two numbers."
    ):
        multiplication.get_result()


def test_invalid_inputs_for_division():
    """Test that Division requires at least two inputs."""
    division = Division(user_id=dummy_user_id(), inputs=[10])
    with pytest.raises(
        ValueError,
        match="Inputs must be a list with at least two numbers."
    ):
        division.get_result()


def test_division_by_zero_in_middle():
    """Test division by zero when zero appears in the middle of inputs."""
    inputs = [100, 5, 0, 2]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division.get_result()


def test_division_by_zero_at_end():
    """Test division by zero when zero is the last input."""
    inputs = [50, 5, 0]
    division = Division(user_id=dummy_user_id(), inputs=inputs)
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        division.get_result()


# Tests Demonstrating Polymorphic Behavior
def test_polymorphic_list_of_calculations():
    """Test that different calculation types can be stored in the same list."""
    user_id = dummy_user_id()
    
    calculations = [
        Calculation.create('addition', user_id, [1, 2, 3]),
        Calculation.create('subtraction', user_id, [10, 3]),
        Calculation.create('multiplication', user_id, [2, 3, 4]),
        Calculation.create('division', user_id, [100, 5]),
    ]
    
    assert isinstance(calculations[0], Addition)
    assert isinstance(calculations[1], Subtraction)
    assert isinstance(calculations[2], Multiplication)
    assert isinstance(calculations[3], Division)
    
    results = [calc.get_result() for calc in calculations]
    assert results == [6, 7, 24, 20]


def test_polymorphic_method_calling():
    """Test that polymorphic methods work correctly."""
    user_id = dummy_user_id()
    inputs = [10, 2]
    
    calc_types = ['addition', 'subtraction', 'multiplication', 'division']
    expected_results = [12, 8, 20, 5]
    
    for calc_type, expected in zip(calc_types, expected_results):
        calc = Calculation.create(calc_type, user_id, inputs)
        result = calc.get_result()
        assert result == expected