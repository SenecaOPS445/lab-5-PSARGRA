#!/usr/bin/env python3
# Author ID: Priyanshu Sargra

def add(number1, number2):
    """
    Adds two numbers together.

    ARGUMENTS:
    number1 (int/str): First number.
    number2 (int/str): Second number.

    RETURNS:
    int: Sum of the two numbers if valid.
    str: 'error: could not add numbers' if inputs are invalid.
    """
    try:
        return int(number1) + int(number2)  # Convert to int and add
    except ValueError:  # Handle case where conversion fails
        return 'error: could not add numbers'


def read_file(filename):
    """
    Reads content from a file.

    ARGUMENTS:
    filename (str): The file name to read.

    RETURNS:
    list: List of lines if file exists.
    str: 'error: could not read file' if an error occurs.
    """
    try:
        with open(filename, 'r') as f:  # Open file in read mode
            return f.readlines()  # Read and return lines as list
    except FileNotFoundError:  # Handle missing file error
        return 'error: could not read file'


if __name__ == '__main__':
    print(add(10, 5))         # Expected: 15
    print(add('10', 5))       # Expected: 15
    print(add('abc', 5))      # Expected: 'error: could not add numbers'

    print(read_file('seneca2.txt'))    # Expected: File content (if exists)
    print(read_file('file10000.txt'))  # Expected: 'error: could not read file'
