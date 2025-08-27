# write_append_file.py

filename = "output.txt"

# 1. Take user input and write it to the file (overwrite mode)
user_input = input("Enter some data to write to the file: ")

with open(filename, 'w') as file:
    file.write(user_input + "\n")

# 2. Append additional data
additional_data = "This is the appended text."
with open(filename, 'a') as file:
    file.write(additional_data + "\n")

# 3. Read and display final content
print(f"\nFinal contents of '{filename}':")
with open(filename, 'r') as file:
    print(file.read())
