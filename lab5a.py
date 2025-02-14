#!/usr/bin/env python3
# Author ID: Priyanshu Sargra

def read_file_string(file_name):
    """Takes a file_name as a string and returns its entire contents as a string."""
    f = open(file_name, 'r')  # Open the file for reading
    content = f.read()  # Read all contents from the file
    f.close()  # Close the file
    return content  # Return the entire file as a string

def read_file_list(file_name):
    """Takes a file_name as a string and returns a list of lines without new-line characters."""
    f = open(file_name, 'r')  # Open the file for reading
    lines = f.readlines()  # Read all lines from the file
    f.close()  # Close the file
    return [line.strip() for line in lines]  # Remove '\n' from each line

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))  # Print the full content as a string
    print(read_file_list(file_name))  # Print file content as a list of lines
