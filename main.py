from worker import Worker
import datetime

def main():
    current_year = datetime.datetime.now().year
    employees = [] 

    print("=== Ввод данных о сотрудниках ===")
    
    count = input("Введите количество сотрудников для ввода: ")
    
    if not count.isdigit() or int(count) <= 0:
        print("Некорректный ввод. Завершение программы.")
        return

    count = int(count)

    for i in range(count):
        print(f"\n--- Ввод данных сотрудника №{i + 1} ---")
        
        name = input("Фамилия и инициалы: ")
        position = input("Должность: ")
        
        salary = input("Зарплата: ")
        salary = float(salary) if salary.replace('.','',1).isdigit() else 0.0
        
        year = input("Год поступления на работу: ")
        year = int(year) if year.isdigit() else current_year

        worker = Worker(name, position, salary, year)
        employees.append(worker)

    target_experience = input("\nВведите стаж работы (в годах) для поиска сотрудников: ")
    
    if not target_experience.isdigit() or int(target_experience) < 0:
         print("Некорректный ввод стажа.")
         return

    target_experience = int(target_experience)

    print("\n=== Результаты поиска ===")
    
    found = False
    
    for emp in employees:
        if emp.get_work_experience() > target_experience:
            emp.display_info() 
            found = True

    if not found:
         print(f"Сотрудников со стажем более {target_experience} лет не найдено.")

if __name__ == "__main__":
    main()