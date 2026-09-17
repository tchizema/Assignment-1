students = {
    "John": 85,
    "Mary": 92,
    "David": 78,
    "Sarah": 95,
    "Peter": 88
}

# Display all students and their marks
print("Students and their marks:")

for name, mark in students.items():
    print(name, ":", mark)

# Find the student with the highest mark
highest_student = max(students, key=students.get)

print("\nStudent with the highest mark:")
print(highest_student, ":", students[highest_student])