
import unittest

from student import Student


class TestStudent(unittest.TestCase):

    def test_calculate_average(self):
        student = Student("Vikas", [80, 90, 70])
        self.assertEqual(student.calculate_average(), 80)

    def test_highest_mark(self):
        student = Student("Vikas", [80, 90, 70])
        self.assertEqual(student.highest_mark(), 90)

    def test_convert_to_dictionary(self):
        student = Student("Vikas", [80, 90, 70])

        self.assertEqual(
            student.to_dict(),
            {"name": "Vikas", "marks": [80, 90, 70]}
        )

    def test_create_student_from_dictionary(self):
        data = {"name": "Rahul", "marks": [70, 80, 90]}
        student = Student.from_dict(data)

        self.assertEqual(student.name, "Rahul")
        self.assertEqual(student.marks, [70, 80, 90])

    def test_reject_invalid_marks(self):
        with self.assertRaises(ValueError):
            Student("Vikas", [80, 120, 70])

    def test_reject_empty_name(self):
        with self.assertRaises(ValueError):
            Student("", [80, 90, 70])


if __name__ == "__main__":
    unittest.main()
