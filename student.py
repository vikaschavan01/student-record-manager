
class Student:
    def __init__(self, name: str, marks: list[int]):
        # Validate student name
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")

        # Validate marks
        if not marks:
            raise ValueError("Marks cannot be empty")

        if any(
            not isinstance(mark, (int, float))
            or isinstance(mark, bool)
            or mark < 0
            or mark > 100
            for mark in marks
        ):
            raise ValueError("Marks must be between 0 and 100")

        self.name = name.strip()
        self.marks = marks.copy()

    def calculate_average(self) -> float:
        """Calculate and return the average of the student's marks."""
        return sum(self.marks) / len(self.marks)

    def highest_mark(self) -> int:
        """Return the highest mark."""
        return max(self.marks)

    def display(self) -> None:
        """Display student details."""
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Highest Mark: {self.highest_mark()}")

    def to_dict(self) -> dict:
        """Convert the student object into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Student object from a dictionary."""
        return cls(data["name"], data["marks"])
