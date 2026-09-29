def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return
    if name in students:
        print(name, "already exists. Updating score ?...")
    try:
        score = float(input(f"Enter score for {name}: "))
    except ValueError:
        print("Invalid score. Please enter a number.")
        return
    students[name] = score
    print(f"Student '{name}' added with score {score}.")


def view_students():
    if not students:
        print("No students found. Please add a student first.")
        return
    print("\n--- Student List ---")
    for name, score in students.items():
        print(f"{name:<20} : {score}")


def search_student():
    if not students:
        print("No students found. Please add a student first.")
        return
    name = input("Enter student name to search: ").strip()
    if name in students:
        print(f"{name} : {students[name]}")
    else:
        print(f"Student '{name}' not found.")


def calculate_average():
    if not students:
        print("No students found. Please add a student first.")
        return
    average = sum(students.values()) / len(students)
    print(f"Average score of all students: {average:.2f}")


def highest_score():
    if not students:
        print("No students found. Please add a student first.")
        return
    name = max(students, key=students.get)
    print(f"Highest score: {name} with {students[name]}")


def lowest_score():
    if not students:
        print("No students found. Please add a student first.")
        return
    name = min(students, key=students.get)
    print(f"Lowest score: {name} with {students[name]}")
    
def pause():
    input("\nPress Enter to return to the main menu...")