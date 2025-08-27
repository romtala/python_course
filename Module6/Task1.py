
marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

# Ask user for student name
student_name = input("Enter student name: ")

# Retrieve and display marks
if student_name in marks:
    print(f"Marks obtained by {student_name}: {marks[student_name]}")
else:
    print(f"Student {student_name} not found.")
