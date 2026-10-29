
from student import Student
from storage import load_students, save_students


def validate_marks(marks: float) -> bool:
    """Check whether marks are within the valid range."""
    return 0 <= marks <= 100


def is_pass(marks: float) -> bool:
    """Return True if marks are at least 40."""
    return validate_marks(marks) and marks >= 40


def validate_student(name: str, marks: list[float]) -> bool:
    """Validate a student's name and three subject marks."""
    return (
        bool(name.strip())
        and len(marks) == 3
        and all(validate_marks(mark) for mark in marks)
    )


def get_marks() -> list[float]:
    marks = []

    for i in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))

                if validate_marks(mark):
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks



def add_student(students: list[Student]) -> None:
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = get_marks()

    if not validate_student(name, marks):
        print("Invalid student data.")
        return

    students.append(Student(name, marks))
    save_students(students)
    print("Student added successfully!")



def view_students(students: list[Student]) -> None:
    if not students:
        print("No student records found.")
        return

    for student in students:
        student.display()


def search_student(students: list[Student]) -> None:
    name = input("Enter name to search: ").strip().casefold()

    if not name:
        print("Please enter a name to search.")
        return

    matches = [
        s for s in students if name in s.name.casefold()
    ]

    if matches:
        for student in matches:
            student.display()
    else:
        print("Student not found.")


def update_student(students: list[Student]) -> None:
    name = input("Enter exact student name to update: ").strip().casefold()
    matches = [s for s in students if s.name.casefold() == name]

    if len(matches) != 1:
        print("Student not found or name is duplicated.")
        return

    print("Enter the new marks.")
    matches[0].marks = get_marks()
    save_students(students)
    print("Marks updated successfully!")


def delete_student(students: list[Student]) -> None:
    name = input("Enter exact student name to delete: ").strip().casefold()
    matches = [s for s in students if s.name.casefold() == name]

    if len(matches) != 1:
        print("Student not found or name is duplicated.")
        return

    confirm = input("Confirm deletion? (yes/no): ").strip().casefold()

    if confirm == "yes":
        students.remove(matches[0])
        save_students(students)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


def class_statistics(students: list[Student]) -> None:
    if not students:
        print("No student records available.")
        return

    averages = [s.calculate_average() for s in students]
    top_student = max(students, key=lambda s: s.calculate_average())

    print("Total students:", len(students))
    print(f"Class average: {sum(averages) / len(averages):.2f}")
    print("Top student:", top_student.name)
    print(f"Top average: {top_student.calculate_average():.2f}")


def data_quality_report(students: list[Student]) -> None:
    if not students:
        print("No student records available.")
        return

    valid_records = 0
    invalid_records = 0
    passed_students = 0
    failed_students = 0

    for student in students:
        if not validate_student(student.name, student.marks):
            invalid_records += 1
            continue

        valid_records += 1

        # A student must pass all three subjects.
        if all(is_pass(mark) for mark in student.marks):
            passed_students += 1
        else:
            failed_students += 1

    print("\n===== DATA QUALITY REPORT =====")
    print("Total records:", len(students))
    print("Valid records:", valid_records)
    print("Invalid records:", invalid_records)
    print("Students passed:", passed_students)
    print("Students failed:", failed_students)



def main() -> None:
    try:
        students = load_students()
    except ValueError as error:
        print(error)
        print("Fix the JSON file before continuing.")
        return

    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Class statistics")
        print("7. Data quality report")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()
        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                class_statistics(students)
            elif choice == "7":
                data_quality_report(students)
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, OSError) as error:
            print("Operation failed:", error)


#Test runs
# print(validate_marks(85))   # True
# print(validate_marks(-10))  # False
# print(validate_marks(150))  # False
# print(calculate_average([80, 90, 70]))
# print(calculate_average([]))

# print(validate_marks(85))  # True
# print(validate_marks(-10))  # False
# print(validate_marks(150))  # False

# print(is_pass(75))  # True
# print(is_pass(35))  # False

# print(validate_student("Rahul", [80, 90, 70]))  # True
# print(validate_student("", [80, 90, 70]))  # False
# print(validate_student("Priya", [80, 90]))  # False
# print(validate_student("Amit", [80, 120, 70]))  # False
#Test runs


if __name__ == "__main__":
    main()
