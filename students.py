class Student:

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades
        self.courses = courses
    pass
    
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    pass

    class StudentRecords:
        def __init__(self):
            self.students = []
        pass

        @classmethod
        def add_student(self, student_id, student_name, email, grades=None, courses=None):
            enroll_student = Student(student_id, student_name, email, grades, courses)
            self.students.append(enroll_student)
            return "Student added successfully"
        pass
        
        @classmethod
        def update_student(self, student_id, email=None, grades=None, courses=None):
            for student in self.students:
                if student.id_name[0] == student_id:
                    if email is not None:
                        student.email = email
                    if grades is not None:
                        student.grades.update(grades)
                    if courses is not None:
                        student.courses.update(courses)
                    return "Student updated successfully"
            return "Student not found"
        pass

        @classmethod
        def delete_student(cls, student_id):
            idlength = len(self.students)
            self.students = [student for student in self.students if student.id_name[0] != student_id]
            if len(self.students) < idlength:
                return "Student deleted successfully"
            return "Student not found"
        pass

        @classmethod
        def enrollcourse(cls, student_id, course):
            for student in self.students:
                if student.id_name[0] == student_id:
                    student.courses.add(course)
                    return "Course enrolled successfully"
            return "Student not found"
        pass

        @classmethod
        def searchstudent(cls, student_id):
            for student in self.students:
                if student.id_name[0] == student_id:
                    return str(student)
            return "Student not found"
            pass

        @classmethod #Challenge 1: Calculate GPA
        def gpa(student):
            if not student.grades:
                return 0.0
            total_points = 0
            for score in self.grades.values():
                if score >= 90:
                    total_points += 4.0
                elif score >= 80:
                    total_points += 3.0
                elif score >= 70:
                    total_points += 2.0
                elif score >= 60:
                    total_points += 1.0
                else:
                    total_points += 0.0
            return total_points / len(self.grades)
        pass
    
        @classmethod
        def search_by_name(self, name):
            results = []
            for student in self.students:
                if name.lower() in student.id_name[1].lower():
                    results.append(str(student))
            return results if results else ["No matches found"]
        pass


# ---------------------------------------------------------------------------------------
# OUTPUTS
# ---------------------------------------------------------------------------------------
rec = Student.StudentRecords() # USED TO ACCESS THE STUDENTRECORDS CLASS

print(rec.add_student(1, "Alice", "alice@mail.com", grades={"History": 85}))
print(rec.add_student(2, "Bob Smith", "bob@mail.com"))
                
