class GradeBook:

    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            return f"Student '{name}' already exists"
        self.students[name] = []
        return f"Student '{name}' added"

    def add_grade(self, name, grade):
        if name not in self.students:
            return f"Student '{name}' not found"
        if not isinstance(grade, (int, float)) or grade < 0:
            return "Invalid grade"
        self.students[name].append(grade)
        return f"Grade {grade} added for student '{name}'"

    def get_average(self, name):
        if name not in self.students:
            return f"Student '{name}' not found"
        grades = self.students[name]
        if not grades:
            return f"No grades available for student '{name}'"
        average = sum(grades) / len(grades)
        return round(average, 2)