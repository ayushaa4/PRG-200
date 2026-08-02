class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A"
        elif avg >= 65:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        avg = self.average()
        result = "Pass" if avg >= 40 else "Fail"

        print("Name:", self.name)
        print("Average:", round(avg, 2))
        print("Grade:", self.grade())
        print("Result:", result)
        print("-" * 30)


students = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

student_list = []

for name, marks in students:
    student_list.append(Student(name, marks))

for student in student_list:
    student.display()