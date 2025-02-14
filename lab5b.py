#!/usr/bin/env python3
# Author ID: Priyanshu Sargra

def read_file_string(file_name):
    """Reads the entire file and returns it as a single string."""
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):
    """Reads a file and returns its content as a list of lines (removes newlines)."""
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    clean_lines = []
    for line in lines:
        clean_lines.append(line.strip())  # Remove newline characters
    return clean_lines

def append_file_string(file_name, string_of_lines):
    """Appends the given string to the end of the file."""
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    """Writes a list of strings to a file, each item on a new line."""
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')  # Write each line and add a newline
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads data from one file, writes to a new file, and adds line numbers."""
    f_read = open(file_name_read, 'r')
    f_write = open(file_name_write, 'w')
    line_num = 1
    for line in f_read:
        f_write.write(f"{line_num}:{line}")  # Prefix each line with its number
        line_num += 1
    f_read.close()
    f_write.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
