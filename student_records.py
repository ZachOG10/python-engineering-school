students = ["Zach", "Peace", "David", "Ajeh", "James"]
for student in students:
    print(student)
students.append("Kator")
students.remove("Zach")
print(f"Total students: {len(students)}")
print(f"Is Zach registered?: {"Zach" in students}")
print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")