import datetime

class Worker:
    def __init__(self, full_name="Неизвестно", position="Стажер", salary=0, year_of_employment=None):
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.year_of_employment = year_of_employment if year_of_employment is not None else datetime.datetime.now().year

    def update_info(self, full_name, position, salary):
        self.full_name = full_name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Сотрудник: {self.full_name}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary} руб.")
        print(f"Год приема: {self.year_of_employment}")
        print("-" * 20)

    def get_work_experience(self, current_year):
        current_year = datetime.datetime.now().year
        return current_year - self.year_of_employment
