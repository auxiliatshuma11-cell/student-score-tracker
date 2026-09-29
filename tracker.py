students.sort(key=lambda student: student["score"], reverse=True)

print("\n STUDENT LEADERBOARD")
print("========================")

for position, student in enumerate(students, start=1):
    print(
        position,
        student["name"],
        "-",
        student["score"],
        "- Grade:",
        student["grade"]
    )