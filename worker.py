import datetime

class Worker:
    """
    Класс для представления информации о сотруднике.
    """
    def __init__(self, full_name="Неизвестно", position="Стажер", salary=0, year_of_employment=None):
        """
        Конструктор класса.
        :param full_name: Фамилия и инициалы работника.
        :param position: Название занимаемой должности.
        :param salary: Зарплата работника.
        :param year_of_employment: Год поступления на работу.
        """
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.year_of_employment = year_of_employment if year_of_employment is not None else datetime.datetime.now().year

    def update_info(self, full_name, position, salary):
        """Метод для изменения данных сотрудника."""
        self.full_name = full_name
        self.position = position
        self.salary = salary

    def display_info(self):
        """Метод для отображения информации о сотруднике."""
        print(f"Сотрудник: {self.full_name}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary} руб.")
        print(f"Год приема: {self.year_of_employment}")
        print("-" * 20)

    def get_work_experience(self, current_year):
        """
        Метод для расчета стажа работы на основе переданного года.
        :param current_year: Текущий год для расчета.
        :return: Стаж работы в годах.
        """
        current_year = datetime.datetime.now().year
        return current_year - self.year_of_employment
