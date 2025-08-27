# read_file.py

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        print(f"Contents of '{filename}':")
        for line in file:
            print(line, end='')  # end='' to avoid double newlines
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
