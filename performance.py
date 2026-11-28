students = [
    ("Zach", 85, "Python"),
    ("John", 90, "Java"),
    ("Mary", 85, "Python"),
    ("David", 75, "Java"),
    ("Sarah", 85, "Python")
]

for student in students:
    print(student)
print("--------------------")

for student in students:
    name, score, course = student

    print(f"Student's name: {name}")
    print(f"Student's score: {score}")
print("--------------------")

scores = (85, 90, 85, 75, 85, 90, 80)

total = scores.count(85)
print(f"Number of students scoring 85: {total}")
print("--------------------")

names = ("Zach", "John", "Mary", "David", "Sarah")

result = names.index("Mary")
print(f"Mary's index: {result}")