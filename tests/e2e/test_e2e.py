import pytest


@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """Test that the homepage displays "Hello World"."""
    page.goto('http://localhost:8000')
    assert page.inner_text('h1') == 'Hello World'


@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """Test the addition functionality of the calculator."""
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    assert page.inner_text('#result') == 'Result: 15'


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """Test the divide by zero functionality of the calculator."""
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'