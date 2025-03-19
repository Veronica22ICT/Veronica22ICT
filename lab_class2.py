from datetime import datetime


class Veronika:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = datetime.now().year
        start_year = 2023
        course = current_year - start_year
        return min(course, 4) if course > 0 else "Не студент"

    def get_name_list(self):
        return [self.first_name, self.last_name]


class AdvancedVeronika(Veronika):
    def __init__(self, first_name=None, last_name=None, birth_year=None, specialty=None, student_id=None,
                 average_grade=None):
        super().__init__(first_name, last_name, birth_year)
        self.specialty = specialty
        self.student_id = student_id
        self.average_grade = average_grade
        self.__secret_info = "Це приватне поле"
        self._protected_info = "Це захищене поле"

    def get_full_info(self):
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Спеціальність": self.specialty,
            "Студентський ID": self.student_id,
            "Середній бал": self.average_grade
        }

    def is_excellent_student(self):
        return self.average_grade is not None and self.average_grade >= 90

    def _get_protected_info(self):
        return self._protected_info

    def __get_secret_info(self):
        return self.__secret_info


advanced_student = AdvancedVeronika("Вероніка", "Матвійчук",
2008, "Інформаційні технології", "12345", 95)
print(advanced_student.calculate_course())
print(advanced_student.get_name_list())
print(advanced_student.get_full_info())
print(advanced_student.is_excellent_student())
