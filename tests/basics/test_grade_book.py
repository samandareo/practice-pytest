from projects.basics.grade_book import GradeBook
import pytest

class TestGradeBook:

    def setup_method(self):
        self.student = GradeBook()

    def test_add_student(self):
        added_student = self.student.add_student("John")
        expected = "Student 'John' added"
        assert added_student == expected

    def test_add_exist_student(self):
        self.student.add_student("Mark")
        added_exist_student = self.student.add_student("Mark")
        expected = "Student 'Mark' already exists"
        assert added_exist_student == expected

    def test_add_grade(self):
        self.student.add_student("Sam")
        graded = self.student.add_grade("Sam", 5)
        expected = "Grade 5 added for student 'Sam'"
        assert graded == expected

    def test_add_grade_for_not_exist_student(self):
        graded = self.student.add_grade("Sam", 5)
        expected = "Student 'Sam' not found"
        assert graded == expected

    def test_add_invalid_grade(self):
        self.student.add_student("Sam")
        assert self.student.add_grade("Sam", "five") == "Invalid grade"
        assert self.student.add_grade("Sam", -5) == "Invalid grade"

    def test_get_average(self):
        self.student.add_student("Tom")
        self.student.add_grade("Tom" , 5)
        self.student.add_grade("Tom", 4)
        self.student.add_grade("Tom", 4)
        avg_grade = self.student.get_average("Tom")
        assert avg_grade == pytest.approx(4.33, 0.01)

    def test_get_average_not_exist_student(self):
        avg_grade = self.student.get_average("Tom")
        expected = "Student 'Tom' not found"
        assert avg_grade == expected

    def test_get_average_not_grades_student(self):
        self.student.add_student("Charlie")
        avg_grade = self.student.get_average("Charlie")
        expected = "No grades available for student 'Charlie'"
        assert avg_grade == expected
