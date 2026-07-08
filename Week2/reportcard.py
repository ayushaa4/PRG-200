grades = []

for i in range(19):
    marks = int(input("Enter marks of Student: "))

    if marks >= 90:
        grades.append("A")
    elif marks >= 80:
        grades.append("B")
    elif marks >= 70:
        grades.append("C")
    elif marks >= 60:
        grades.append("D")
    else:
        grades.append("F")

print("\nGrade Sheet")

for i in range(19):
    print("Student", i+1, ":", grades[i])