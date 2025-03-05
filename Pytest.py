# Unit testing in Python with pytest
# To write unit tests with pytest, we create functions that start with test_ and use assert statements to check the expected outcomes.
# Import the pytest module
import pytest

# Functions to be tested
def add(a, b):
    # Function to add two numbers
    return a + b

def multiply(a, b):
    # Function to multiply two numbers
    return a * b

# Unit test functions
# Test functions should start with 'test_' to be automatically discovered by pytest
def test_add():
    # Test cases for the add function
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2, 2) == 4
    assert add(0, 0) == 0  # Additional test case

def test_add_floats():
    # Test case for the add function with float inputs
    assert add(2.5, 3.1) == 5.6
    assert add(1.5, 2.2) == 3.7  # Additional test case

def test_multiply():
    # Test cases for the multiply function
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0  # Additional test case

def test_multiply_floats():
    # Test case for the multiply function with float inputs
    assert multiply(2.5, 3.1) == 7.75
    assert multiply(1.5, 2.0) == 3.0  # Additional test case