
import json
from pathlib import Path

from student import Student

FILE_PATH = Path(__file__).with_name("students.json")


def load_students() -> list[Student]:
    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Student data must be a JSON list.")

        return [Student.from_dict(record) for record in data]

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Could not load student records: {error}"
        ) from error


def save_students(students: list[Student]) -> None:
    data = [student.to_dict() for student in students]

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
