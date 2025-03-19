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


student = Veronika("Вероніка", "Матвійчук", 2008)
print('Курс:',student.calculate_course())
print(student.get_name_list())

