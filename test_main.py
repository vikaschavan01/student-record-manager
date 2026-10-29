
import unittest

from main import validate_marks, is_pass, validate_student


class TestStudentValidation(unittest.TestCase):

    def test_valid_marks(self):
        self.assertTrue(validate_marks(85))

    def test_negative_marks(self):
        self.assertFalse(validate_marks(-10))

    def test_marks_above_100(self):
        self.assertFalse(validate_marks(120))

    def test_passing_marks(self):
        self.assertTrue(is_pass(75))

    def test_failing_marks(self):
        self.assertFalse(is_pass(35))

    def test_valid_student(self):
        self.assertTrue(
            validate_student("Rahul", [80, 90, 70])
        )

    def test_empty_student_name(self):
        self.assertFalse(
            validate_student("", [80, 90, 70])
        )

    def test_incomplete_marks(self):
        self.assertFalse(
            validate_student("Priya", [80, 90])
        )


if __name__ == "__main__":
    unittest.main()
