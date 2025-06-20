from tasks import TaskManager

manager = TaskManager()
manager.load_tasks()

def print_menu():
    print("\nМеню:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить задачу")
    print("5. Выйти")

def print_tasks(tasks):
    if not tasks:
        print("\n📭 Список задач пуст.")
    else:
        print("\n📋 Ваши задачи:")
        print("---------------------------")
        for i, task in enumerate(tasks, 1):
            status = '✔' if task.completed else '✘'
            print(f'{i:>2}. {task.title:^20} [{status}]')
        print("---------------------------")

while True:
    print_menu()
    choice = input('Ваш выбор: ')
    
    if choice == '1':
        print_tasks(manager.tasks)
        #manager.show_tasks()

    elif choice == '2':
        task = input("Введите текст задачи: ")
        manager.add_task(task)
        manager.save_tasks()
        print("✅ Задача добавлена.")

    elif choice == '3':
        try:
            index = int(input("Введите номер задачи для удаления: "))
            manager.delete_task(index)
            manager.save_tasks()
            print("🗑 Задача удалена.")
        except ValueError:
            print("Введите корректный номер.")
    elif choice == '4':
        try:
            index = int(input("Введите номер задачи для выполнения: "))
            manager.complete_task(index)
            manager.save_tasks()
            print("✅ Задача отмечена как выполненная.")
        except ValueError:
            print("Введите корректный номер.")


    elif choice == '5':
        manager.save_tasks()
        print("До свидания!")
        break

    else:
        print("Неверный выбор, попробуйте снова.")


