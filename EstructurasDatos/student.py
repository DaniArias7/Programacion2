class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


