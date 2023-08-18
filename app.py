from EstructurasDatos.student import Student

student_data = [
    {"name": "Diego", "age": 22, "grades": [4.5, 3.0, 2.1]},
    {"name": "Melanie", "age": 19, "grades": [4.0, 4.6, 5.0]},
    {"name": "Sofia", "age": 18, "grades": [3.8, 5.0, 4.8]}
]

students = [Student(data["name"], data["age"], for data in student_data]

threshold = 85
passing_students = [student for student in students if student.average_grade() >= threshold]

high_achievers = {student.name: student for student in students if student.average_grade() > threshold}

print("All Students:")
for student in students:
    print(f"{student.name} - Age: {student.age} - Grades: {student.grades} - Average Grade: {student.average_grade()}")

print("\nPassing Students:")
for student in passing_students:
    print(f"{student.name} - Age: {student.age} - Grades: {student.grades} - Average Grade: {student.average_grade()}")

print("\nHigh Achievers:")
for name, student in high_achievers.items():
    print(f"{name} - Age: {student.age} - Grades: {student.grades} - Average Grade: {student.average_grade()}")
