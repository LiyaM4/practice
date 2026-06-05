import unittest
from worker import Worker  

class TestWorkerClass(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Иванов И.И.", "Программист", 100000, 2020)

    def test_initial_attributes(self):
        self.assertEqual(self.worker.full_name, "Иванов И.И.")
        self.assertEqual(self.worker.position, "Программист")
        self.assertEqual(self.worker.salary, 100000)
        self.assertEqual(self.worker.year_of_employment, 2020)

    def test_update_info_method(self):
        self.worker.update_info("Петров П.П.", "Старший программист", 120000)
        self.assertEqual(self.worker.full_name, "Петров П.П.")
        self.assertEqual(self.worker.position, "Старший программист")
        self.assertEqual(self.worker.salary, 120000)

    def test_get_work_experience_method(self):
        # Предположим, что текущий год 2026. Стаж должен быть 6 лет.
        # Мы передаем 2026 год как аргумент, чтобы тест не зависел от реальной даты.
        experience = self.worker.get_work_experience(2026) 
        self.assertEqual(experience, 6)

if __name__ == '__main__':
    unittest.main()