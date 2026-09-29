students = []

name = input("Enter student name: ")
score = float(input("Enter student score: "))

student = {
    "name": name,
    "score": score
}

students.append(student)

print("\nStudent Score")
print("----------------")
print("Name:", name)
print("Score:", score)